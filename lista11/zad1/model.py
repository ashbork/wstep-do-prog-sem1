from typing import List, Literal, NewType, Tuple, Union
from mutagen.mp3 import EasyMP3
import pathlib


class Model():
    def __init__(self) -> None:
        self.currenttags = []
        self.tagtuple = ('title', 'album', 'artist',
                         'tracknumber', 'genre', 'date')

    def get_tags_from_file(self, path) -> Tuple[int, str] | List[str] | None:
        if not path:
            # returns None which causes file loading to stop - no file was picked
            return None
        if not path.exists():
            # returns an error code and the context, nonexistent file
            return (-1, path)  # Tuple[int, str]
        if not path.suffix == ".mp3":
            # returns an error code and the context, non-mp3 file
            return (-2, path)  # Tuple[int, str]
        song = EasyMP3(path)
        tags = []
        for key in self.tagtuple:
            if key in song.keys():
                tags.append(song[key][0])
            else:
                tags.append("")
        self.currenttags = tags
        return tags  # List[str]

    def update_tags_in_file(self, path, content: str, tagno: int) -> Literal[-3, 0]:
        tag = self.tagtuple[tagno]
        song = EasyMP3(path)
        if (tag == "date" and not valid_date(content)) or (tag == "tracknumber" and not content.isnumeric()):
            return -3
        song[tag] = content
        song.save()
        return 0

    @staticmethod
    def rename_file(path, new="", auto=False) -> pathlib.Path:
        if auto:
            song = EasyMP3(path)
            return path.rename(pathlib.Path(path.parent, f"{song['title'][0]} by {song['artist'][0]}{path.suffix}"))
        return path.rename(pathlib.Path(path.parent, f"{new}{path.suffix}"))


ModelType = NewType('Model', Model)


def valid_date(date):
    return len(date) > 4 or not date.isnumeric()
