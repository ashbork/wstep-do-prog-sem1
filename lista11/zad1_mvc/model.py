from mutagen.mp3 import EasyMP3
from mutagen.easyid3 import EasyID3
import pathlib


class Model():
    @staticmethod
    def get_tags_from_file(path):
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
        return tags

    @staticmethod
    def update_tags_in_file(path, content: str, tagno):
        nums_to_tags = {
            0: "title",
            1: "album",
            2: "artist",
            3: "tracknumber",
            4: "genre",
            5: "date",
        }
        tag = nums_to_tags[tagno]
        song = EasyMP3(path)
        if (tagno == 5 and not valid_date()) or (tagno == 3 and not content.isnumeric()):
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


def valid_date(date):
    return len(date) > 4 or not date.isnumeric()
