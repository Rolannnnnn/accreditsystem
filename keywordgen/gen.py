import helper
import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import defaultdict

# Folder containing all JSON files
json_folder = "jsons"

texts = []
labels = []

for filename in os.listdir(json_folder):
    filepath = os.path.join(json_folder, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)
        for item in data:
            ocr = item['ocr_text']
            texts.append(helper.clean_ocr_text(ocr))
            labels.append(item['label'])

print(f"Loaded {len(texts)} documents from {json_folder}.")

# Step 2: TF-IDF vectorization with n-grams up to 3
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words='english',
    ngram_range=(1,3)
)
tfidf_matrix = vectorizer.fit_transform(texts)
feature_names = vectorizer.get_feature_names_out()

# Step 3: Build per-document keyword weights
doc_keyword_weights = []
for doc_idx in range(len(texts)):
    tfidf_vector = tfidf_matrix[doc_idx].tocoo()
    word_weights = {feature_names[i]: w for i, w in zip(tfidf_vector.col, tfidf_vector.data)}
    doc_keyword_weights.append(word_weights)

# Step 4: Build per-label aggregated keyword dictionary
label_keyword_dict = defaultdict(lambda: defaultdict(float))

for doc_idx, label in enumerate(labels):
    for word, weight in doc_keyword_weights[doc_idx].items():
        label_keyword_dict[label][word] += weight

# Step 5: Convert defaultdict to normal dict for JSON serialization
label_keyword_dict = {label: dict(keywords) for label, keywords in label_keyword_dict.items()}

# Step 6: Save to JSON
output_file = "label_keywords.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(label_keyword_dict, f, indent=4)

print(f"Saved label keyword dictionary to {output_file}.")