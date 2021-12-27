
import sys
import pathlib
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import eyed3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        """
        UI logic - describes the layout and content of the main window.
        """
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 500)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.current_file = None
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        # 'select file' button
        self.pick_file = QPushButton(self.centralwidget)
        self.pick_file.setObjectName(u"pick_file")
        self.pick_file.setGeometry(QRect(25, 440, 450, 30))
        self.pick_file.setAutoFillBackground(False)
        self.pick_file.setText(u"Select file...")
        self.pick_file.clicked.connect(self.file_dialog)
        # 'rename' button, disabled until a file is selected
        self.rename = QPushButton(self.centralwidget)
        self.rename.setGeometry(QRect(25, 410, 450, 30))
        self.rename.setText(u"Rename file")
        self.rename.setDisabled(True)
        self.rename.clicked.connect(self.rename_file)
        # autorename button, disabled until a file is selected
        self.autorename = QPushButton(self.centralwidget)
        self.autorename.setGeometry(QRect(25, 380, 450, 30))
        self.autorename.setText(u"Autorename file ('<title> by <artist>')")
        self.autorename.setDisabled(True)
        self.autorename.clicked.connect(self.autorename_file)

        # table containing all of the tags - the first column serves as a header
        # while the second is populated with content after a file is loaded
        self.tag_table = QTableWidget(self.centralwidget)
        self.tag_table.setRowCount(3)
        self.tag_table.setColumnCount(2)

        __headertitle = TagHeader("Title")
        self.tag_table.setItem(0, 0, __headertitle)
        __headeralbum = TagHeader("Album")
        self.tag_table.setItem(1, 0, __headeralbum)
        __headerartist = TagHeader("Artist")
        self.tag_table.setItem(2, 0, __headerartist)

        __contenttitle = EditableTags("")
        self.tag_table.setItem(0, 1, __contenttitle)
        __contentalbum = EditableTags("")
        self.tag_table.setItem(1, 1, __contentalbum)
        __contentartist = EditableTags("")
        self.tag_table.setItem(2, 1, __contentartist)
        # styling for the table
        self.tag_table.setObjectName(u"tag_table")
        self.tag_table.setGeometry(QRect(25, 70, 450, 300))
        self.tag_table.setFrameShadow(QFrame.Plain)
        self.tag_table.setLineWidth(1)
        self.tag_table.setAlternatingRowColors(False)
        self.tag_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerItem)
        self.tag_table.setShowGrid(True)
        self.tag_table.setGridStyle(Qt.SolidLine)
        self.tag_table.setCornerButtonEnabled(False)

        self.tag_table.horizontalHeader().setVisible(False)
        self.tag_table.horizontalHeader().setHighlightSections(True)
        self.tag_table.horizontalHeader().setStretchLastSection(True)
        self.tag_table.verticalHeader().setVisible(False)
        # a label showing the current working file
        self.file_indicator = QLabel(self.centralwidget)
        self.file_indicator.setObjectName(u"file_indicator")
        self.file_indicator.setGeometry(QRect(25, 20, 450, 30))
        self.file_indicator.setAlignment(Qt.AlignCenter)
        self.file_indicator.setText(u"Currently not editing any file. Select a file to edit its tags.")

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setWindowTitle(u"MP3 Tag Editor")

    @Slot()
    def save_new_tags(self, *args):
        """
        Saves values that were changed in the table to the current working .mp3 file.
        """
        indices_to_tags = {
            0: "title",
            1: "album",
            2: "artist",
        }
        if self.current_file:
            song = eyed3.load(self.current_file)
            if args[0] == 0:
                song.tag.title = self.tag_table.item(args[0], args[1]).text()
            if args[0] == 1:
                song.tag.album = self.tag_table.item(args[0], args[1]).text()
            if args[0] == 2:
                song.tag.artist = self.tag_table.item(args[0], args[1]).text()
            song.tag.save()

    @Slot()
    def file_dialog(self) -> str:
        """
        Opens a file dialog that allows the user to choose an .mp3 file. If not cancelled,
        it calls the file handler and allows it to update the UI to match the change.
        """
        picker = QFileDialog(
            main_window, "Select .mp3 file...", QDir.currentPath())
        picker.setFileMode(QFileDialog.AnyFile)
        picker.setNameFilter("*.mp3")
        files = []
        if picker.exec():
            files = picker.selectedFiles()
        if files:
            return self.handle_new_file(files[0])

    def update_fname_indicator(self):
        """
        Updates the file indicator.
        """
        filename = self.current_file.name
        self.file_indicator.setText(f"Currently editing \'{filename[:30] + '...' if len(filename) > 30 else filename}\'")

    def handle_new_file(self, path: str):
        """
        Contains all of the logic managing:
        - updating the filename indicator
        - enabling the rename buttons
        - populating the tag table
        - connecting the cellChanged signal to save_new_tags()

        Args:
            path (str): path to the current file, obtained from the file dialog
        """
        self.current_file = pathlib.Path(path)
        self.update_fname_indicator()
        self.rename.setDisabled(False)
        self.autorename.setDisabled(False)
        song = eyed3.load(self.current_file)
        taglist = [song.tag.title, song.tag.album, song.tag.artist]
        for index, tag in enumerate(taglist):
            __content = EditableTags(tag)
            self.tag_table.setItem(index, 1, __content)
        self.tag_table.cellChanged.connect(self.save_new_tags)

    @Slot()
    def rename_file(self):
        """
        Asks user for input, then renames the current working file accordingly. Calls on_rename_success() on success.
        """
        dialog = QInputDialog(main_window)
        dialog.setInputMode(QInputDialog.InputMode.TextInput)
        dialog.setLabelText("Enter new name")
        if dialog.exec():
            self.current_file = self.current_file.rename(pathlib.Path(self.current_file.parent, f"{dialog.textValue()}{self.current_file.suffix}"))
            self.update_fname_indicator()
            self.on_rename_success()

    @Slot()
    def autorename_file(self):
        """
        Renames the current working file according to the pattern. Calls on_rename_success() on success.
        """
        song = eyed3.load(self.current_file)
        self.current_file = self.current_file.rename(pathlib.Path(self.current_file.parent, f"{song.tag.title} by {song.tag.artist}{self.current_file.suffix}"))
        self.update_fname_indicator()
        self.on_rename_success()

    def on_rename_success(self):
        messagebox = QMessageBox(QMessageBox.Icon.Information, "Renaming was successful", f"Renamed file to {self.current_file.name}")
        messagebox.exec()


class TagHeader(QTableWidgetItem):
    """
    Subclass of QTableWidgetItem that is uneditable.
    """
    def __init__(self, content) -> None:
        super().__init__()
        self.setText(content)
        self.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable)


class EditableTags(QTableWidgetItem):
    """
    Subclass of QTableWidgetItem. Is editable and selectable.
    """
    def __init__(self, content) -> None:
        super().__init__()
        self.setText(content)
        self.setFlags(Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEditable)


if __name__ == "__main__":
    app = QApplication()
    main_window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec())
