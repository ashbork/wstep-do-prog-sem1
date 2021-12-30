from beartype import beartype
from model import ModelType
from view import ViewType

class Controller():
    @beartype
    def __init__(self, model: ModelType, view: ViewType) -> None:
        self.file_loaded = False
        self.currentworkingpath = ""
        self.model = model
        self.view = view

        self.view.pick_file.clicked.connect(self.on_file_btn)
        self.view.tag_table.cellChanged.connect(self.on_field_update)
        self.view.autorename.clicked.connect(self.on_autorename_btn)
        self.view.rename.clicked.connect(self.on_rename_btn)

    def on_file_btn(self):
        self.file_loaded = False
        self.currentworkingpath = self.view.file_dialog()
        tags = self.model.get_tags_from_file(self.currentworkingpath)
        if tags is None:
            pass
        elif isinstance(tags[0], int):
            self.view.error_message(*tags)
        else:
            self.view.update_fname_indicator(self.currentworkingpath)
            self.view.draw_new_fields(tags)
            self.view.enable_rename_buttons()
            self.file_loaded = True

    def on_field_update(self, *indices):
        tagnum = indices[0]
        if not self.file_loaded:
            return
        if self.model.update_tags_in_file(self.currentworkingpath, self.view.get_field_value(*indices), indices[0]) == -3:
            self.view.error_message(-3)
            self.view.revert_change(*indices, content=self.model.currenttags[tagnum])

    def on_rename_btn(self):
        newname = self.view.rename_dialog()
        if newname in (None, ""):
            return
        self.currentworkingpath = self.model.rename_file(self.currentworkingpath, newname)
        self.view.update_fname_indicator(self.currentworkingpath)
        self.view.rename_successful(self.currentworkingpath)
        print(self.currentworkingpath)

    def on_autorename_btn(self):
        self.currentworkingpath = self.model.rename_file(self.currentworkingpath, auto=True)
        self.view.update_fname_indicator(self.currentworkingpath)
        self.view.rename_successful(self.currentworkingpath)
        print(self.currentworkingpath)
