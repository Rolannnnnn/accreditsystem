import sys
import modelengine, keywordengine, helper
from typeselector import TypeSelectorWindow
from typeselectorpic import TypeSelectorPicWindow
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QProgressDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from ui_selection import Ui_MainWindow
import os
from PIL import Image
from PyPDF2 import PdfReader
import pytesseract
import pdf2image

class SelectionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Example: connect button
        self.ui.chooseBttn.clicked.connect(self.select_file)
        self.ui.processBttn.clicked.connect(self.process_file)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select a file",
            "",  # start directory
            "Images (*.png *.jpg *.jpeg);; PDF Files (*.pdf);; All Files (*.*)"
        )
        if file_path:
            self.selected_file = file_path
            self.ui.pathEdit.setText(file_path)
            print("Selected file:", self.selected_file)

            valid = self.is_valid_image_or_pdf(file_path)
            if valid:
                pixmap = QPixmap(file_path)
                if not pixmap.isNull():
                    scaled_pixmap = pixmap.scaled(self.ui.imageframe.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
                    self.ui.imageframe.setPixmap(scaled_pixmap)
                else:
                    self.ui.imageframe.setText("Cannot display preview.")
            else:
                self.ui.imageframe.setText("Invalid file selected.")

    def process_file(self):
        valid = self.is_valid_image_or_pdf(self.ui.pathEdit.text())

        if self.ui.isImageCB.isChecked():
            if not valid:
                helper.show_invalid_file_dialog(
                    self,
                    "Invalid File",
                    "Please select a valid image file (PNG, JPG, etc.) or a PDF file."
                )
            else:
                self.type_selector_window = TypeSelectorPicWindow(self.ui.pathEdit.text())
                self.type_selector_window.show()
            return

        progress = QProgressDialog("Processing file...", "Cancel", 0, 100, self)
        progress.setWindowTitle("Please wait")
        progress.setWindowModality(Qt.WindowModal)
        progress.show()
        QApplication.processEvents()
        progress.setValue(0)
        progress.setValue(10)

        if not valid:
            helper.show_invalid_file_dialog(
                self,
                "Invalid File",
                "Please select a valid image file (PNG, JPG, etc.) or a PDF file."
            )
        else:
            text = self.ocr(self.ui.pathEdit.text())
            progress.setValue(50)
            if text == "":
                helper.show_invalid_file_dialog(
                    self,
                    "OCR Failed",
                    "The selected file could not be processed. Please try another file."
                )
            else:
                print("Extracted Text:", text)
                keywordresult = keywordengine.keyword_run(text)
                progress.setValue(75)
                modelresult = modelengine.model_run(text)
                progress.setValue(100)
                self.type_selector_window = TypeSelectorWindow(keywordresult, modelresult, self.ui.pathEdit.text())
                self.type_selector_window.show()
        progress.close()

    # Check if file_path points to a valid image or PDF file.
    def is_valid_image_or_pdf(self, file_path: str) -> bool:
        if not os.path.isfile(file_path):
            return False
        ext = os.path.splitext(file_path)[1].lower()
        valid_image_exts = {".png", ".jpg", ".jpeg", ".bmp", ".gif", ".tiff", ".webp"}
        valid_pdf_exts = {".pdf"}
        if ext in valid_image_exts:
            try:
                with Image.open(file_path) as img:
                    img.verify()
                return True
            except Exception:
                return False
        elif ext in valid_pdf_exts:
            try:
                reader = PdfReader(file_path)
                _ = reader.metadata
                return True
            except Exception:
                return False
        return False
    
    # Checks if arrays are non-empty
    def are_nonempty_arrays(x, y):
        def is_nonempty_array(obj):
            return (
                obj is not None
                and isinstance(obj, (list, tuple, np.ndarray))
                and len(obj) > 0
            )

        return is_nonempty_array(x) and is_nonempty_array(y)
    
    # OCR function
    def ocr(self, filepath: str):
        text_result = ""
        try:
            ext = os.path.splitext(filepath)[1].lower()

            if ext in [".png", ".jpg", ".jpeg", ".bmp", ".tiff"]:
                # Process image directly
                image = Image.open(filepath)
                text_result = pytesseract.image_to_string(image)

            elif ext == ".pdf":
                # Try converting first page
                pages = pdf2image.convert_from_path(filepath, first_page=1, last_page=1)
                if pages:
                    text_result = pytesseract.image_to_string(pages[0])
                else:
                    text_result = ""

            else:
                # Unsupported file type — treat as empty
                text_result = ""

            # Clean text if helper is available
            text_result = helper.clean_ocr_text(text_result)
            return text_result.strip()

        except Exception as e:
            # Suppress all OCR or file-related errors — return blank string
            helper.show_invalid_file_dialog(self, "OCR Error", f"An error occurred during OCR processing:\n{e}")
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SelectionWindow()
    window.show()
    sys.exit(app.exec())