from beartype import beartype
from model import ModelType
from view import ViewType


class Controller():
    # typecheck, if any of these two aren't of correct types
    # beartype throws an exception and stops the app from running
    @beartype
    def __init__(self, model: ModelType, view: ViewType) -> None:
        self.file_loaded = False
        self.currentworkingpath = ""
        self.model = model
        self.view = view

        # ignoring all type hints here - for some reason .clicked/.cellChanged aren't
        # recognized as members of widgets, no clue as to why that is
        self.view.pick_file.clicked.connect(self.on_file_btn)  # type: ignore
        self.view.tag_table.cellChanged.connect(self.on_field_update)  # type: ignore
        self.view.autorename.clicked.connect(self.on_autorename_btn)  # type: ignore
        self.view.rename.clicked.connect(self.on_rename_btn)  # type: ignore

    def on_file_btn(self) -> None:
        self.file_loaded = False
        self.currentworkingpath = self.view.file_dialog()
        tags = self.model.get_tags_from_file(self.currentworkingpath)
        if tags is None:
            pass
        elif isinstance(tags, tuple):
            self.view.error_message(*tags)
        else:
            self.view.update_fname_indicator(
                self.currentworkingpath)  # type: ignore
            self.view.draw_new_fields(tags)
            self.view.enable_rename_buttons()
            self.file_loaded = True

    def on_field_update(self, *indices) -> None:
        tagnum = indices[0]
        if not self.file_loaded:
            return
        if self.model.update_tags_in_file(self.currentworkingpath, self.view.get_field_value(*indices), indices[0]) == -3:
            self.view.error_message(-3)
            self.view.revert_change(
                *indices, content=self.model.currenttags[tagnum])

    def on_rename_btn(self) -> None:
        newname = self.view.rename_dialog()
        if newname in (None, ""):
            return
        self.currentworkingpath = self.model.rename_file(
            self.currentworkingpath, newname)
        self.view.update_fname_indicator(self.currentworkingpath)
        self.view.rename_successful(self.currentworkingpath)

    def on_autorename_btn(self) -> None:
        self.currentworkingpath = self.model.rename_file(
            self.currentworkingpath, auto=True)
        self.view.update_fname_indicator(self.currentworkingpath)
        self.view.rename_successful(self.currentworkingpath)
        print(self.currentworkingpath)
