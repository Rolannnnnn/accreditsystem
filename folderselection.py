from ui_folderselection import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QCheckBox, QVBoxLayout
import helper
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem
import sys
import json
import os
import shutil

class FolderSelectorWindow(QMainWindow):
    def __init__(self, type, filepath, jsonpath):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.type = type
        self.filepath = filepath
        self.jsonpath = jsonpath
        self.load_checklist(self.jsonpath, self.type)
        self.ui.comboBox.lineEdit().setReadOnly(True)

        self.ui.confirmBttn.clicked.connect(lambda: self.copy_selected_files(self.filepath))
        self.ui.cancelBttn.clicked.connect(self.close)
        self.ui.modeswitch.valueChanged.connect(lambda: self.filter_checkboxes(None))

    def load_checklist(self, json_path, selected_type):
        # Load JSON
        with open(json_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        # map display_path -> {'description': str, 'constraints': set()}
        path_map = {}
        unique_constraints = set()

        # Parse JSON 
        for area_name, area_data in data.items():
            for param_name, param_data in area_data.items():
                for section_name, section_data in param_data.items():
                    if not isinstance(section_data, dict):
                        continue

                    for node_key, node_value in section_data.items():
                        # node_value could be dict of subkeys
                        if not isinstance(node_value, dict):
                            continue
                        sub_containers = [(sub_k, sub_v) for sub_k, sub_v in node_value.items() if isinstance(sub_v, dict)]

                        # Remember description of node 0
                        zero_desc = ""
                        for sk, sd in sub_containers:
                            if sk == "0":
                                zero_desc = sd.get("description", "").strip()
                                break

                        for sub_key, sub_data in sub_containers:
                            # Build display path (skip showing "> 0")
                            if sub_key == "0":
                                path = f"{area_name} > {param_name} > {section_name} > {node_key}"
                            else:
                                path = f"{area_name} > {param_name} > {section_name} > {node_key} > {sub_key}"

                            # Build description, append 0's description if applicable
                            raw_desc = sub_data.get("description", "").strip()
                            if sub_key == "0":
                                description = raw_desc  # use as-is
                            else:
                                # prepend the zero's description
                                if zero_desc:
                                    description = f"{zero_desc} {raw_desc}"
                                else:
                                    description = raw_desc

                            # iterate documents
                            for doc in sub_data.get("document", []):
                                if doc.get("type") == selected_type:
                                    # ensure path entry exists
                                    if path not in path_map:
                                        path_map[path] = {"description": description, "constraints": set()}
                                    # add document's constraints to this path
                                    for c in doc.get("constraint", []):
                                        if c:
                                            path_map[path]["constraints"].add(c)
                                            unique_constraints.add(c)

        # Prepare checklist entries as (path, description, [constraints])
        checklist_entries = []
        for path, info in path_map.items():
            checklist_entries.append((path, info.get("description", ""), sorted(info.get("constraints", []))))

        # Clear existing widgets in the scroll area's inner layout
        layout = self.ui.scrollAreaWidgetContents.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.scrollAreaWidgetContents)
            self.ui.scrollAreaWidgetContents.setLayout(layout)
        else:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                    widget.deleteLater()

        # Populate checkboxes and store them with their constraints
        self.checkboxes = []
        for path, description, constraints in checklist_entries:
            cb = QCheckBox(path)
            cb.setToolTip(description or "No description available.")
            cb.setChecked(True)
            layout.addWidget(cb)
            # store (checkbox, list_of_constraints)
            self.checkboxes.append((cb, list(constraints)))

        # Block signals while populating
        self.ui.comboBox.blockSignals(True)
        self.ui.comboBox.clear()

        # Create a model for checkable items
        model = QStandardItemModel()

        # Optionally, you can still add "All" as a first item
        all_item = QStandardItem("All")
        all_item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
        all_item.setData(Qt.Checked, Qt.CheckStateRole)  # default checked
        model.appendRow(all_item)

        # Add each unique constraint as a checkable item
        for constraint in sorted(unique_constraints):
            item = QStandardItem(constraint)
            item.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
            item.setData(Qt.Unchecked, Qt.CheckStateRole)  # default unchecked
            model.appendRow(item)

        # Assign the model to the combo box
        self.ui.comboBox.setModel(model)
        self.ui.comboBox.blockSignals(False)

        # Listen for item changes
        model = self.ui.comboBox.model()
        model.itemChanged.connect(self.filter_checkboxes)

        self.constraints = sorted(unique_constraints)

    def filter_checkboxes(self, changed_item):
        model = self.ui.comboBox.model()

        if changed_item:
            # Handle "All" item logic
            all_item = model.item(0)
            if changed_item == all_item:
                if all_item.checkState() == Qt.Checked:
                    for row in range(1, model.rowCount()):
                        model.item(row).setCheckState(Qt.Unchecked)
                    for cb, _ in self.checkboxes:
                        cb.setChecked(True)
                        cb.show()
                else:
                    pass
                return
            if changed_item and changed_item != all_item:
                if changed_item.checkState() == Qt.Checked:
                    if all_item.checkState() == Qt.Checked:
                        all_item.setCheckState(Qt.Unchecked)
        
        # Collect all checked constraints (skip "All")
        selected_constraints = []
        for row in range(model.rowCount()):
            item = model.item(row)
            if item.text() == "All":
                all_item = item
                continue
            if item.checkState() == Qt.Checked:
                selected_constraints.append(item.text())
        
        # If "All" is checked or nothing selected, show all checkboxes
        if all_item.checkState() == Qt.Checked or not selected_constraints:
            for cb, _ in self.checkboxes:
                cb.show()
                cb.setChecked(True)
            return
        
        # Controls the checkbox filtering mode: OR (0) / AND (1)
        modeswitch = self.ui.modeswitch.value()

        if modeswitch == 0:
            for cb, constraints in self.checkboxes:
                if any(c in constraints for c in selected_constraints):
                    cb.show()
                    cb.setChecked(True)
                else:
                    cb.hide()
                    cb.setChecked(False)
        else:
            for cb, constraints in self.checkboxes:
                if all(c in constraints for c in selected_constraints):
                    cb.show()
                    cb.setChecked(True)
                else:
                    cb.hide()
                    cb.setChecked(False)
        
        self.updateComboText()

    def updateComboText(self):
        model = self.ui.comboBox.model()

        checked_items = []
        for row in range(1, model.rowCount()):
            item = model.item(row)
            if item.checkState() == Qt.Checked:
                checked_items.append(item.text())

        # If none checked → show "All"
        if not checked_items:
            self.ui.comboBox.lineEdit().setText("All")
            return

        # If too many, show "n selected"
        if len(checked_items) > 2:
            self.ui.comboBox.lineEdit().setText(f"{len(checked_items)} selected")
            return

        # Otherwise show the checked items joined
        self.ui.comboBox.lineEdit().setText(", ".join(checked_items))

    def copy_selected_files(self, filepath):
        if not os.path.isfile(filepath):
            helper.show_invalid_file_dialog(self, "Error", f"The file does not exist:\n{filepath}")
            return

        # ✅ Save inside user's Documents folder
        documents_dir = os.path.join(os.path.expanduser("~"), "Documents", "Accreditation Copies")
        os.makedirs(documents_dir, exist_ok=True)

        copied_count = 0
        debug_logs = []

        for cb, _ in self.checkboxes:
            if cb.isChecked():
                parts = [p.strip() for p in cb.text().split(">")]
                dest_dir = os.path.join(documents_dir, *parts)

                try:
                    os.makedirs(dest_dir, exist_ok=True)

                    filename = os.path.basename(filepath)
                    dest_path = os.path.join(dest_dir, filename)

                    # Avoid overwriting existing files
                    if os.path.exists(dest_path):
                        base, ext = os.path.splitext(filename)
                        count = 1
                        while os.path.exists(dest_path):
                            dest_path = os.path.join(dest_dir, f"{base}_{count}{ext}")
                            count += 1

                    shutil.copy(filepath, dest_path)
                    copied_count += 1
                    debug_logs.append(f"✔ Copied to: {dest_path}")

                except Exception as e:
                    debug_logs.append(f"❌ Failed to copy to {dest_dir}: {e}")

        # Print all debug logs to console
        print("\n".join(debug_logs) or "⚠ No folders were selected or copied.")

        # Final popup message
        helper.show_info_dialog(
            self,
            "Copy Complete",
            f"Copied to {copied_count} folder(s).\n\n"
            f"Files saved under your Documents/Accreditation Copies folder."
            if copied_count > 0 else "No folders were selected."
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FolderSelectorWindow()
    window.show()
    sys.exit(app.exec())