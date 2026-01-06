import os
import json
from collections import defaultdict

# Path to your main folder containing NER JSONs
NER_FOLDER = "ner"  # adjust if needed

def extract_doc_expectations(ner_folder):
    doc_expectations = defaultdict(set)

    # Iterate over each subfolder (doc type)
    for doc_type in os.listdir(ner_folder):
        doc_path = os.path.join(ner_folder, doc_type)
        if not os.path.isdir(doc_path):
            continue

        # Iterate over JSON files inside each doc_type folder
        for filename in os.listdir(doc_path):
            if not filename.endswith(".json"):
                continue

            json_path = os.path.join(doc_path, filename)
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)

                # Extract NER labels
                ner_labels = data.get("ner_labels", [])

                # Collect all unique entity types for this doc type
                for label in ner_labels:
                    if label != "O":
                        # Remove "B-" or "I-" prefix if exists
                        clean_label = label.split("-", 1)[-1] if "-" in label else label
                        doc_expectations[doc_type].add(clean_label.lower())

    # Convert sets to sorted lists
    doc_expectations = {k: sorted(list(v)) for k, v in doc_expectations.items()}
    return doc_expectations

if __name__ == "__main__":
    DOC_EXPECTATIONS = extract_doc_expectations(NER_FOLDER)
    print("DOC_EXPECTATIONS = ", DOC_EXPECTATIONS)

    # Optional: save to a Python file
    with open("doc_expectations.py", "w", encoding="utf-8") as f:
        f.write("DOC_EXPECTATIONS = ")
        f.write(json.dumps(DOC_EXPECTATIONS, indent=4))