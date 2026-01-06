import helper
import json
import os
import sys
from sklearn.feature_extraction.text import TfidfVectorizer

def get_base_path():
    """Get the base path for resources, works for both dev and PyInstaller."""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        return sys._MEIPASS
    else:
        # Running in normal Python environment
        return os.path.dirname(os.path.abspath(__file__))

def keyword_run(text):
    labels = keyword_score_document(text)
    types = helper.label_to_type(labels)
    return types

def keyword_score_document(text):
    # Load the label keyword JSON
    base_path = get_base_path()
    keywords_path = os.path.join(base_path, "keywords.json")
    with open(keywords_path, "r", encoding="utf-8") as f:
        label_keywords = json.load(f)

    # Tokenize using the same n-grams (1-3)
    vectorizer = TfidfVectorizer(lowercase=True, stop_words='english', ngram_range=(1,3))
    vectorizer.fit([text])
    doc_tokens = vectorizer.get_feature_names_out()

    # Score each label
    label_scores = {}
    for label, keywords in label_keywords.items():
        score = 0.0
        for token in doc_tokens:
            if token in keywords:
                score += keywords[token]
        label_scores[label] = score

    # Get top 5 labels
    top_labels = sorted(label_scores.items(), key=lambda x: x[1], reverse=True)[:5]
    rawlabels = []

    print("Top matching labels for document:")
    for label, score in top_labels:
        print(f"{label}: {score:.2f}")
        rawlabels.append(label)
    return rawlabels