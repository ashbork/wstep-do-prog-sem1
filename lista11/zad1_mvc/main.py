from ui import Ui_MainWindow as ui
from model import Model
from PySide6 import QtWidgets, QtCore
import sys


class Controller():
    def __init__(self) -> None:
        self.file_loaded = False
        self.currentworkingpath = ""
        view.pick_file.clicked.connect(self.on_file_btn)
        view.tag_table.cellChanged.connect(self.on_field_update)
        view.autorename.clicked.connect(self.on_autorename_btn)
        view.rename.clicked.connect(self.on_rename_btn)

    @QtCore.Slot()
    def on_file_btn(self):
        if self.file_loaded:
            self.file_loaded = False
        self.currentworkingpath = view.file_dialog()
        tags = Model.get_tags_from_file(self.currentworkingpath)
        if tags is None:
            pass
        elif isinstance(tags[0], int):
            view.error_message(*tags)
        else:
            view.update_fname_indicator(self.currentworkingpath)
            view.draw_new_fields(tags)
            view.enable_rename_buttons()
            self.file_loaded = True

    def on_field_update(self, *indices):
        tagnum = indices[0]
        if not self.file_loaded:
            return
        if Model.update_tags_in_file(self.currentworkingpath, view.get_field_value(*indices), indices[0]) == -3:
            view.error_message(-3)
            view.revert_change(*indices, content=Model.get_tags_from_file(self.currentworkingpath)[tagnum])

    def on_rename_btn(self):
        newname = view.rename_dialog()
        if newname in (None, ""):
            return
        self.currentworkingpath = Model.rename_file(self.currentworkingpath, newname)
        view.update_fname_indicator(self.currentworkingpath)
        view.rename_successful(self.currentworkingpath)
        print(self.currentworkingpath)

    def on_autorename_btn(self):
        self.currentworkingpath = Model.rename_file(self.currentworkingpath, auto=True)
        view.update_fname_indicator(self.currentworkingpath)
        view.rename_successful(self.currentworkingpath)
        print(self.currentworkingpath)


if __name__ == "__main__":
    app = QtWidgets.QApplication()
    main_window = QtWidgets.QMainWindow()
    view = ui(main_window)
    controller = Controller()
    model = Model
    main_window.show()
    sys.exit(app.exec())
