from PySide6.QtWidgets import QMessageBox
import re

def show_invalid_file_dialog(self, title, text):
    msg = QMessageBox(self)
    msg.setIcon(QMessageBox.Warning)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

def show_info_dialog(self, title, text):
    msg = QMessageBox(self)
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(title)
    msg.setText(text)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

def clean_ocr_text(text):
    """
    Aggressively clean OCR text for any document type while preserving
    meaningful words, numbers, dates, grades, and key phrases.
    """

    # Normalize whitespace
    text = " ".join(text.split())

    # Remove repeated symbols (e.g., ----====, X-X-X-X)
    text = re.sub(r'([^\w\s])(?:\1[-\1]*){3,}', ' ', text)

    # Remove sequences of symbols that are likely garbage (≥5 chars)
    text = re.sub(r'\b[^\w\s]{5,}\b', ' ', text)

    # Remove very short nonsense tokens (1-2 chars of symbols only)
    text = re.sub(r'\b[^\w\s]{1,2}\b', ' ', text)

    # Remove stray punctuation surrounded by whitespace (like " , " or " ; ")
    text = re.sub(r'\s[^\w\s]\s', ' ', text)

    # Remove multiple consecutive non-alphanumeric symbols inside words
    text = re.sub(r'(?<=\w)[^\w\s]{2,}(?=\w)', '', text)

    # Remove stray non-printable/control characters
    text = re.sub(r'[\x00-\x1F\x7F]', '', text)

    # Final cleanup: collapse multiple spaces
    text = " ".join(text.split())

    return text