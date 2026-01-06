import helper
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AutoModelForTokenClassification
import torch
import os
import sys
import torch.nn.functional as F
import doc_expectations as de

def model_run(text):
    # Get classifier predictions with confidence scores
    classification_results = classify_text(text)
    
    # Extract entities using NER model
    detected_entities = extract_entities_ner(text)
    
    # Adjust confidence scores based on entity matching
    adjusted_results = adjust_confidence_with_ner(classification_results, detected_entities)
    
    # Convert to types and extract confidence levels
    labels = [label for label, _ in adjusted_results]
    confidences = [confidence for _, confidence in adjusted_results]
    types = helper.label_to_type(labels)
    return types, confidences

# Get the correct base path for both development and PyInstaller executable
def get_base_path():
    """Get the base path for resources, works for both dev and PyInstaller."""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        return sys._MEIPASS
    else:
        # Running in normal Python environment
        return os.getcwd()

# Load your fine-tuned model from the local "model" folder
base_path = get_base_path()
model_path = os.path.join(base_path, "model")

tokenizer = AutoTokenizer.from_pretrained(model_path, local_files_only=True)
model = AutoModelForSequenceClassification.from_pretrained(model_path, local_files_only=True)

# Load NER model from the local "ner_model" folder
ner_model_path = os.path.join(base_path, "ner_model")
ner_tokenizer = AutoTokenizer.from_pretrained(ner_model_path, local_files_only=True)
ner_model = AutoModelForTokenClassification.from_pretrained(ner_model_path, local_files_only=True)

def classify_text(text: str):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )

    # Predict
    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    probs = F.softmax(logits, dim=-1)[0]  # probabilities for each class

    # Get top 5
    top5_prob, top5_idx = torch.topk(probs, 5)

    results = []
    for i in range(5):
        class_id = top5_idx[i].item()
        confidence = top5_prob[i].item()
        label = model.config.id2label[class_id]
        results.append((label, confidence))

    print("Top 5 predictions from the classifier:")
    for label, confidence in results:
        print(f"{label}: {confidence:.4f}")
    
    return results


def extract_entities_ner(text: str):
    """
    Extract named entities from text using the NER model.
    Returns a dict of entity types to list of detected entities.
    """
    # Tokenize input
    inputs = ner_tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512,
        return_offsets_mapping=True
    )
    
    offset_mapping = inputs.pop("offset_mapping")[0]
    
    # Predict
    with torch.no_grad():
        outputs = ner_model(**inputs)
    
    # Get predictions
    predictions = torch.argmax(outputs.logits, dim=-1)[0]
    tokens = ner_tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
    
    # Aggregate entities with proper WordPiece token reconstruction
    entities = {}
    current_entity_type = None
    current_word = ""
    
    for idx, (token, pred_id) in enumerate(zip(tokens, predictions)):
        if token in ["[CLS]", "[SEP]", "[PAD]"]:
            continue
            
        label = ner_model.config.id2label[pred_id.item()]
        
        # Handle BIO tagging scheme
        if label.startswith("B-"):
            # Save previous entity if exists
            if current_entity_type and current_word:
                if current_entity_type not in entities:
                    entities[current_entity_type] = []
                entities[current_entity_type].append(current_word.strip())
            
            # Start new entity
            current_entity_type = label[2:].lower()  # Remove "B-" prefix
            # Handle WordPiece tokens: remove ## prefix if present
            if token.startswith("##"):
                current_word = token[2:]
            else:
                current_word = token
            
        elif label.startswith("I-"):
            # Continue current entity
            entity_type = label[2:].lower()
            if entity_type == current_entity_type and current_entity_type:
                # Append to current word, handling WordPiece tokens
                if token.startswith("##"):
                    current_word += token[2:]  # No space for subword tokens
                else:
                    current_word += " " + token  # Space for new word
            else:
                # Entity type changed, save previous and start new
                if current_entity_type and current_word:
                    if current_entity_type not in entities:
                        entities[current_entity_type] = []
                    entities[current_entity_type].append(current_word.strip())
                current_entity_type = entity_type
                if token.startswith("##"):
                    current_word = token[2:]
                else:
                    current_word = token
        else:
            # O tag or end of entity
            if current_entity_type and current_word:
                if current_entity_type not in entities:
                    entities[current_entity_type] = []
                entities[current_entity_type].append(current_word.strip())
            current_entity_type = None
            current_word = ""
    
    # Save last entity if exists
    if current_entity_type and current_word:
        if current_entity_type not in entities:
            entities[current_entity_type] = []
        entities[current_entity_type].append(current_word.strip())
    
    # Clean up entities: remove fragments, punctuation, and very short entities
    cleaned_entities = {}
    for entity_type, entity_list in entities.items():
        cleaned_list = []
        for entity in entity_list:
            # Remove leading/trailing punctuation and whitespace
            entity_clean = entity.strip().strip('.,;:!?()[]{}"\'-')
            
            # Skip if empty after cleaning
            if not entity_clean:
                continue
            
            # Skip if only punctuation
            if all(c in '.,;:!?()[]{}"\'-/\\|@#$%^&*+=~`<> \t\n' for c in entity_clean):
                continue
            
            # Skip very short fragments (likely tokenization errors) unless they're meaningful
            if len(entity_clean) <= 2 and not entity_clean.isdigit():
                continue
            
            cleaned_list.append(entity_clean)
        
        if cleaned_list:  # Only add if there are valid entities
            cleaned_entities[entity_type] = cleaned_list
    
    print("\nEntities detected by NER:")
    for entity_type, entity_list in cleaned_entities.items():
        print(f"{entity_type}: {entity_list}")
    
    return cleaned_entities


def adjust_confidence_with_ner(classification_results, detected_entities):
    """
    Adjust confidence scores based on NER entity matching.
    70% weight from classifier, 30% weight from NER entity matching.
    """
    adjusted_results = []
    
    for label, classifier_confidence in classification_results:
        # Get expected entities for this label
        expected_entities = de.DOC_EXPECTATIONS.get(label, [])
        
        if not expected_entities:
            # No expected entities, keep original confidence
            adjusted_results.append((label, classifier_confidence))
            continue
        
        # Calculate NER score based on entity matching
        matched_count = 0
        total_expected = len(expected_entities)
        
        for expected_entity in expected_entities:
            # Check if this entity type was detected
            if expected_entity in detected_entities and len(detected_entities[expected_entity]) > 0:
                matched_count += 1
        
        # Calculate NER score (0 to 1)
        ner_score = matched_count / total_expected if total_expected > 0 else 1.0
        
        # Apply 70-30 split: 70% classifier, 30% NER
        adjusted_confidence = (0.7 * classifier_confidence) + (0.3 * ner_score)
        
        print(f"\n{label}:")
        print(f"  Classifier confidence: {classifier_confidence:.4f}")
        print(f"  NER score: {ner_score:.4f} ({matched_count}/{total_expected} entities matched)")
        print(f"  Adjusted confidence: {adjusted_confidence:.4f}")
        
        adjusted_results.append((label, adjusted_confidence))
    
    # Re-sort by adjusted confidence
    adjusted_results.sort(key=lambda x: x[1], reverse=True)
    
    print("\n" + "="*50)
    print("Final rankings after NER adjustment:")
    for label, confidence in adjusted_results:
        print(f"{label}: {confidence:.4f}")
    
    return adjusted_results