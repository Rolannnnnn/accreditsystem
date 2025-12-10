from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QRadioButton, QButtonGroup
from ui_typeselectionpic import Ui_MainWindow
import helper
import folderselection
import sys
import json

class TypeSelectorPicWindow(QMainWindow):
    def __init__(self, filepath, logged_user):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.filepath = filepath
        self.logged_user = logged_user

        input_file = "picfolder.json"
        with open(input_file, "r", encoding="utf-8") as f:
            data = json.load(f)

        types = set()

        for area in data.values():
            for parameter in area.values():
                for section in parameter.values():
                    for node in section.values():
                        for subnode in node.values():
                            if "document" in subnode:
                                for doc in subnode["document"]:
                                    if "type" in doc:
                                        types.add(doc["type"])

        set1 = sorted(types)

        # Create a container widget for the scroll area
        scroll_content = QWidget()
        scroll_content_layout = QVBoxLayout(scroll_content)
        scroll_content.setLayout(scroll_content_layout)
        # Add your radio buttons to the scroll_content_layout
        self.radio_group = QButtonGroup(self)
        self.radio_group.setExclusive(True)
        self.add_radio_buttons(scroll_content_layout, set1)
        # Assign the widget to the scroll area
        self.ui.scrollArea.setWidget(scroll_content)
        self.ui.scrollArea.setWidgetResizable(True)

        self.radio_group.buttonClicked.connect(self.on_radio_clicked)

        # --- Connect buttons ---
        self.ui.confirmBttn.clicked.connect(self.confirm_selection)
        self.ui.cancelBttn.clicked.connect(self.back)

    def back(self):
        import selection
        self.MainWindow = selection.SelectionWindow(self.logged_user)
        self.MainWindow.show()
        self.close()

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
            self.Folder_selector_window = folderselection.FolderSelectorWindow(selected_button.text(), self.filepath, "picfolder.json", self.logged_user)
            self.Folder_selector_window.show()
            self.close()
        else:
            helper.show_info_dialog(self, "No Selection", "No Type Selected.")
            return False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TypeSelectorPicWindow()
    window.show()
    sys.exit(app.exec())