import os
from PyQt5.QtWidgets import QTreeView, QFileSystemModel, QWidget, QVBoxLayout


class Explorer(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.file_system_model = QFileSystemModel()
        self.file_system_model.setRootPath(".")
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.file_system_model)
        self.tree_view.setRootIndex(self.file_system_model.index("."))
        self.tree_view.setAnimated(False)
        self.tree_view.setIndentation(20)
        self.tree_view.setSortingEnabled(True)

        layout = QVBoxLayout()
        layout.addWidget(self.tree_view)

        self.setLayout(layout)
