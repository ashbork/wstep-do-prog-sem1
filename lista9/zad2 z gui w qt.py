import pathlib
import sys
from PySide6 import QtCore, QtWidgets, QtGui


class Search_Files(QtWidgets.QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.button = QtWidgets.QPushButton("Check path...")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.text = QtWidgets.QLabel("Select a directory to see items...")

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.dialog_window)

    @QtCore.Slot()
    def dialog_window(self) -> str:
        dirpicker = QtWidgets.QFileDialog(
            self, "Select directory", QtCore.QDir.currentPath())
        dirpicker.setFileMode(QtWidgets.QFileDialog.Directory)
        dirpicker.exec()
        print(dirpicker.selectedFiles())
        return self.search_path_for_workfiles(dirpicker.selectedFiles()[0])

    @QtCore.Slot()
    def search_path_for_workfiles(self, path):
        # First, get the current working directory and append the path parameter.
        subdir = pathlib.Path(path)
        print(subdir)
        # Using a list comprehension, return a list of stringified paths relative to the subdirectory (subdir) which are both
        # .pdf files and contain "praca" in their name.
        results = ""
        for result in [str(child.relative_to(subdir)) for child in subdir.rglob("*.pdf") if "praca" in child.name.lower()]:
            results += result + "\n"
        self.text.setText(results)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Search_Files()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
