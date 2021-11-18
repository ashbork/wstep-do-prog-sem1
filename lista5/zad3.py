class Student:
    def __init__(self, fname, lname, index, list_of_courses):
        """
        Konstruktor klasy przyjmuje imię, nazwisko, nr indeksu i listę z nazwami kursów.

            self: odniesienie do siebie jako obiektu
            fname (string): imię
            lname: (string): nazwisko
            index (string): nr. indeksu
            list_of_courses (list): lista stringów z nazwami kursów

        Z pomocą dictionary comprehension konstruktor tworzy słownik, w którym kluczem jest nazwa przedmiotu a
        wartością pusta lista, co pozwala nam operować na ocenach."""
        if not index.isdecimal() or len(index) != 6:
            print("Podany indeks jest nieprawidłowego formatu lub długości")
        self.fname = fname.title()
        self.lname = lname.title()
        self.index = index
        self.grade_tables = {course: [] for course in list_of_courses}

    def add_grade(self, grade, course):
        """
        Dodanie oceny jest możliwe przez podanie jako argument liczby (int/double) lub krotki (tuple)
        oraz nazwy kursu.

            grade (int/double/tuple): ocena do dodania
            course (str): kurs, do którego należy dodać ocenę

        'Łapiemy' KeyError jeśli kurs nie występuje jako klucz w słowniku grade_tables obiektu"""
        try:
            if isinstance(grade, tuple):
                for grad in grade:
                    self.grade_tables[course].append(grad)
            else:
                self.grade_tables[course].append(grade)
        except KeyError:
            print(f"Student nie uczęszcza na {course} / taki kurs nie istnieje")

    def edit_grade(self, course):
        if self.grade_tables[course]:
            self.display_grades(course)
            grade_index = int(input("Którą z tych ocen chcesz edytować? "))
            if grade_index > len(self.grade_tables[course]) - 1:
                print("Nie ma oceny o takim indeksie oceny ")
            else:
                newgrade = int(input("Jaką ocena powinna tu trafić? "))
                self.grade_tables[course][grade_index] = newgrade
                print("Oceny po zmianie: ")
                self.display_grades(course)
        else:
            print(f"W kursie {course} nie ma ocen. ")

    def display_grades(self, course):
        try:
            if self.grade_tables[course]:
                print(f"Wyświetlam oceny z kursu: {course}")
                for index, grade in enumerate(self.grade_tables[course]):
                    # Użyty enumerate w celu pokazania indeksów oraz ocen pod nimi
                    print(f"Ocena nr {index}: {grade}")
            else:
                print(f"W kursie {course} nie ma ocen. ")
        except KeyError:
            print(f"Student nie uczęszcza na {course} / taki kurs nie istnieje")


jan = Student("Jan", "Kowalski", "123456", ["Analiza Matematyczna", "Miernictwo", "Programowanie"])
jan.add_grade((1, 3, 2), "Programowandsaie")
jan.edit_grade("Programowanie")
jan.display_grades("Analiza Matematyczna")
