import json
import datetime
import pathlib


class Diary:
    def __init__(self, filename: str = "default") -> None:
        """
        Generates new instance of the Diary class. If passed a filename, it will attempt to load the associated .json file within
        the current working directory.
        If one doesn't exist, it'll create a new file with an empty list, ready to be worked on.

        Args:
            filename (str): the filename of a file containing entries.
        """        
        self.file = pathlib.Path.cwd() / f"{filename}.json"
        print(self.file)
        if self.file.exists():
            self._load_diary()
            print(f"Plik {filename}.json już istniał, wczytuję...")
        else:
            print(f"Plik {filename}.json wcześniej nie istniał, tworzę...")
            self.entries = []
            self._save_diary()

    def add_entry(self, content: str) -> None:
        """
        Adds an entry to the diary, appending it to the entries list and saving.

        Args:
            content (str): content of the new entry.
        """        
        self.entries.append({
            "date_and_time": datetime.datetime.now().strftime("%c"),
            "content": content
        })
        self._save_diary()

    def read_all_entries(self, desc: bool = True) -> None:
        """
        Reads all entries of the diary. Allows for different sorting options.

        Args:
            desc (bool): decides whether the output should be ascending or descending (by entry's date of creation). 
        """
        if not self.entries: print("W pliku nie ma jeszcze żadnych wpisów.");
        for index, entry in enumerate(sorted(self.entries, key=lambda entry: entry["date_and_time"], reverse=desc)):
            print(index+1, entry["date_and_time"], entry["content"])

    def _save_diary(self) -> None:
        """
        Private method that saves the entries to file.
        """        
        with open(self.file, "w") as cwf:
            json.dump(self.entries, cwf)

    def _load_diary(self) -> None:
        """
        Private method that saves the entries to file.
        """        
        with open(self.file, "r") as cwf:
            self.entries = json.load(cwf)


def interface_with_diary():
    """
    Provides an terminal user interface for the Diary class.
    """    
    current_working_diary = Diary(
        input("Podaj nazwę pliku, na którym chcesz pracować.\n"))
    while (choice := input("Jakie działania na pliku chcesz podjąć? \n 1. Dodaj wpis \n 2. Wyświetl wszystkie wpisy \n 3. Zamknij pamiętnik i wyjdź z programu\n")) != "3":
        if choice == "1":
            current_working_diary.add_entry(
                input("Podaj treść nowego wpisu. \n"))
        elif choice == "2":
            desc = True if input(
                "1. nowe wpisy pierwsze \n2. starsze wpisy pierwsze\n") == "1" else False
            current_working_diary.read_all_entries(desc)
        else:
            print("Nieprawidłowa opcja, spróbuj jeszcze raz.\n")


interface_with_diary()
