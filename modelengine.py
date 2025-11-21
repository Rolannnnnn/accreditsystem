import helper
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import os
import torch.nn.functional as F

def model_run(text):
    labels = classify_text(text)
    types = helper.label_to_type(labels)
    return types

# Load your fine-tuned model from the local "model" folder
model_path = os.path.join(os.getcwd(), "model")

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)

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

    labels = []
    print("Top 5 predictions from the model:")
    for label, confidence in results:
        print(f"{label}: {confidence:.4f}")
        labels.append(label)
    return labels