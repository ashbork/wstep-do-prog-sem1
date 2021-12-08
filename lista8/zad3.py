try:
    with open("zad1.txt", "r") as file:
        content = file.read()
        print("Zawartość pliku:\n" + content)
        query = input("Podaj frazę, której szukasz\n")
        print(f"Znalazłem {query} w pliku {content.count(query)} raz{'' if content.count(query) == 1 else 'y'}.") if\
            query in content else print(f"Nie znalazłem {query} w pliku.")
        print(f"W pliku jest {len(content)} znaków")
except FileNotFoundError:
    print("Plik nie istnieje.")
