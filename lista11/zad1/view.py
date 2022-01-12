from PySide6 import QtWidgets, QtCore
import pathlib
from typing import NewType


class View(object):
    def __init__(self, MainWindow):
        """
        UI logic - describes the layout and content of the main window.
        """
        # qt window whispering
        self.window = QtWidgets.QMainWindow()
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setWindowTitle(u"MP3 Tag Editor")

        # 'select file' button
        self.pick_file = QtWidgets.QPushButton(self.centralwidget)
        self.pick_file.setObjectName(u"pick_file")
        self.pick_file.setGeometry(QtCore.QRect(25, 440, 450, 30))
        self.pick_file.setAutoFillBackground(False)
        self.pick_file.setText(u"Select file...")

        # 'rename' button, disabled until a file is selected
        self.rename = QtWidgets.QPushButton(self.centralwidget)
        self.rename.setGeometry(QtCore.QRect(25, 410, 450, 30))
        self.rename.setText(u"Rename file")
        self.rename.setDisabled(True)

        # autorename button, disabled until a file is selected
        self.autorename = QtWidgets.QPushButton(self.centralwidget)
        self.autorename.setGeometry(QtCore.QRect(25, 380, 450, 30))
        self.autorename.setText(u"Autorename file ('<title> by <artist>')")
        self.autorename.setDisabled(True)

        # table containing all of the tags - the first column serves as a header
        # while the second is populated with content after a file is loaded
        self.tag_table = QtWidgets.QTableWidget(self.centralwidget)
        self.tag_table.setRowCount(6)
        self.tag_table.setColumnCount(2)

        # populate headers (0th col)
        __headertitle = Header("Title")
        self.tag_table.setItem(0, 0, __headertitle)
        __headeralbum = Header("Album")
        self.tag_table.setItem(1, 0, __headeralbum)
        __headerartist = Header("Artist")
        self.tag_table.setItem(2, 0, __headerartist)
        __headertracknum = Header("Track Num")
        self.tag_table.setItem(3, 0, __headertracknum)
        __headergenre = Header("Genre")
        self.tag_table.setItem(4, 0, __headergenre)
        __headeryear = Header("Year")
        self.tag_table.setItem(5, 0, __headeryear)

        # populate fields (1st col)
        __contenttitle = EditableField("")
        self.tag_table.setItem(0, 1, __contenttitle)
        __contentalbum = EditableField("")
        self.tag_table.setItem(1, 1, __contentalbum)
        __contentartist = EditableField("")
        self.tag_table.setItem(2, 1, __contentartist)
        __contenttracknum = EditableField("")
        self.tag_table.setItem(3, 1, __contenttracknum)
        __contentgenre = EditableField("")
        self.tag_table.setItem(4, 1, __contentgenre)
        __contentyear = EditableField("")
        self.tag_table.setItem(5, 1, __contentyear)

        # styling for the table
        self.tag_table.setObjectName(u"tag_table")
        self.tag_table.setGeometry(QtCore.QRect(25, 70, 450, 300))
        self.tag_table.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tag_table.setLineWidth(1)
        self.tag_table.setAlternatingRowColors(False)
        self.tag_table.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tag_table.setShowGrid(True)
        self.tag_table.setGridStyle(QtCore.Qt.SolidLine)
        self.tag_table.setCornerButtonEnabled(False)
        self.tag_table.horizontalHeader().setVisible(False)
        self.tag_table.horizontalHeader().setHighlightSections(True)
        self.tag_table.horizontalHeader().setStretchLastSection(True)
        self.tag_table.verticalHeader().setVisible(False)

        # a label showing the current working file
        self.file_indicator = QtWidgets.QLabel(self.centralwidget)
        self.file_indicator.setObjectName(u"file_indicator")
        self.file_indicator.setGeometry(QtCore.QRect(25, 20, 450, 30))
        self.file_indicator.setAlignment(QtCore.Qt.AlignCenter)  # type: ignore
        self.file_indicator.setText(
            u"Currently not editing any file. Select a file to edit its tags.")

    def file_dialog(self) -> pathlib.Path | None:
        """
        Opens a file dialog that allows the user to choose an .mp3 file. If not cancelled,
        it calls the file handler and allows it to update the UI to match the change.
        """
        picker = QtWidgets.QFileDialog(
            self.window, "Select .mp3 file...", QtCore.QDir.currentPath())
        picker.setFileMode(QtWidgets.QFileDialog.AnyFile)
        picker.setNameFilter("*.mp3")
        if picker.exec():
            return pathlib.Path(picker.selectedFiles()[0])
        return None

    def draw_new_fields(self, tags: None | list[str]) -> None:
        if not tags:
            return
        for index, tag in enumerate(tags):
            __content = EditableField(tag)
            self.tag_table.setItem(index, 1, __content)

    def error_message(self, err_code: int, context: str = ""):
        errors = {
            -1: f"file {context} doesn't exist",
            -2: f"file {context} isn't a valid .mp3 file",
            -3: "incorrect format, tag wasn't saved"
        }
        messagebox = QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Icon.Critical, "Error", errors[err_code])
        messagebox.exec()

    def rename_successful(self, name: pathlib.Path):
        messagebox = QtWidgets.QMessageBox(
            QtWidgets.QMessageBox.Icon.Information, "Renaming was successful", f"Renamed file to {name}")
        messagebox.exec()

    def update_fname_indicator(self, path: pathlib.Path):
        """
        Updates the file indicator.
        """
        filename = path.name
        self.file_indicator.setText(
            f"Currently editing \'{filename[:30] + '...' if len(filename) > 30 else filename}\'")

    def get_field_value(self, row, col):
        return self.tag_table.item(row, col).text()

    def revert_change(self, row, col, content):
        self.tag_table.item(row, col).setText(content)

    def rename_dialog(self):
        dialog = QtWidgets.QInputDialog(self.window)
        dialog.setInputMode(QtWidgets.QInputDialog.InputMode.TextInput)
        dialog.setLabelText("Enter new name")
        if dialog.exec():
            return dialog.textValue()

    def enable_rename_buttons(self):
        self.rename.setDisabled(False)
        self.autorename.setDisabled(False)


class Header(QtWidgets.QTableWidgetItem):
    """
    Subclass of QTableWidgetItem that is uneditable.
    """

    def __init__(self, content) -> None:
        super().__init__()
        self.setText(content)
        self.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled |
                      QtCore.Qt.ItemFlag.ItemIsSelectable)  # type: ignore


class EditableField(QtWidgets.QTableWidgetItem):
    """
    Subclass of QTableWidgetItem. Is editable and selectable.
    """

    def __init__(self, content) -> None:
        super().__init__()
        self.setText(content)
        self.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled |
                      QtCore.Qt.ItemFlag.ItemIsEditable)  # type: ignore


ViewType = NewType('View', View)
