import json
import datetime

class Diary:
    def __init__(self, filename:str) -> None:
        self.filename = filename
        try:
            with open(f"{filename}.json", "r"):
                self._load_diary()
                print("file already exists, cool")
                
        except FileNotFoundError:
            print("file didn't exist yet")
            self.entries = []
            self._save_diary()
            
    def add_entry(self, content:str):
        entry = {
            "date_and_time": datetime.datetime.now().strftime("%c"),
            "content": content
        }
        self.entries.append(entry)
        self._save_diary()
    
    def read_all_entries(self):
        pass

    def _save_diary(self):
        with open(f"{self.filename}.json", "w") as cwd:
                json.dump(self.entries, cwd)
    
    def _load_diary(self):
        with open(f"{self.filename}.json", "r") as cwd:
                self.entries = json.load(cwd)
        
moj_pamietnik = Diary("abc")
moj_pamietnik.add_entry("jazdaaunia")