from typing import NewType
from mutagen.mp3 import EasyMP3
import pathlib


class Model():
    def __init__(self) -> None:
        self.currenttags = []

    def get_tags_from_file(self, path):
        if not path:
            return None
        if not path.exists():
            return (-1, path)
        if not path.suffix == ".mp3":
            return (-2, path)
        song = EasyMP3(path)
        tags = []
        for key in ('title', 'album', 'artist', 'tracknumber', 'genre', 'date'):
            if key in song.keys():
                tags.append(song[key][0])
            else:
                tags.append("")
        self.currenttags = tags
        return tags

    @staticmethod
    def update_tags_in_file(path, content: str, tagno):
        nums_to_tags = ("title", "album", "artist", "tracknumber", "genre", "date")
        tag = nums_to_tags[tagno]
        song = EasyMP3(path)
        if (tag == "date" and not valid_date(content)) or (tag == "tracknumber" and not content.isnumeric()):
            return -3
        song[tag] = content
        song.save()
        return 0

    @staticmethod
    def rename_file(path, new="", auto=False):
        if auto:
            song = EasyMP3(path)
            return path.rename(pathlib.Path(path.parent, f"{song['title'][0]} by {song['artist'][0]}{path.suffix}"))
        return path.rename(pathlib.Path(path.parent, f"{new}{path.suffix}"))

ModelType = NewType('Model', Model)
def valid_date(date):
    return len(date) > 4 or not date.isnumeric()
