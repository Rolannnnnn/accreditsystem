from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QRadioButton, QButtonGroup
from ui_typeselection import Ui_MainWindow
import helper
import folderselection
import sys

class TypeSelectorWindow(QMainWindow):
    def __init__(self, keyword, model, filepath):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        set1 = set(keyword)
        set2 = set(model)

        self.filepath = filepath

        common = list(set1 & set2)
        unique1 = list(set1 - set2)
        unique2 = list(set2 - set1)

        # --- Single button group for all radios ---
        self.radio_group = QButtonGroup(self)
        self.radio_group.setExclusive(True)

        # --- Add radios to three separate containers ---
        self.add_radio_buttons(self.ui.vlayoutbest, common)
        self.add_radio_buttons(self.ui.vlayoutkeyword, unique1)
        self.add_radio_buttons(self.ui.vlayoutmodel, unique2)

        # --- Connect signal for all radios ---
        self.radio_group.buttonClicked.connect(self.on_radio_clicked)

        # --- Connect buttons ---
        self.ui.confirmBttn.clicked.connect(self.confirm_selection)
        self.ui.cancelBttn.clicked.connect(self.close)

    def add_radio_buttons(self, container: QWidget, choices: list):
        """Adds a list of radio buttons to a layout and links them to one group."""
        layout = container.layout()
        if layout is None:
            layout = QVBoxLayout(container)
            container.setLayout(layout)

        # Clear old buttons
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # Add new radio buttons
        for i, choice in enumerate(choices):
            radio = QRadioButton(choice)
            layout.addWidget(radio)
            self.radio_group.addButton(radio)

    def on_radio_clicked(self, button):
        print(f"Selected: {button.text()}")

    def confirm_selection(self):
        selected_button = self.radio_group.checkedButton()

        if selected_button is not None:
            print(f"✅ One selected: {selected_button.text()}")
            self.Folder_selector_window = folderselection.FolderSelectorWindow(selected_button.text(), self.filepath)
            self.Folder_selector_window.show()
        else:
            helper.show_info_dialog(self, "No Selection", "No Type Selected.")
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TypeSelectorWindow()
    window.show()
    sys.exit(app.exec())