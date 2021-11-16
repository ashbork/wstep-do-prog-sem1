class Student:
    def __init__(self, fname, lname, index, list_of_courses):
        if not index.isdecimal() or len(index) != 6:
            print("Podany indeks jest nieprawidłowego formatu lub długości")
        self.fname = fname.title()
        self.lname = lname.title()
        self.index = index
        self.grade_tables = {course:[] for course in list_of_courses}

    def add_grade(self, grade, course):
        if isinstance(grade, tuple):
            for grad in grade:
                self.grade_tables[course].append(grad)
        else:
            self.grade_tables[course].append(grade)
        return

    def edit_grade(self, course):
        if self.grade_tables[course]:
            self.display_grades(course)
            grade_index = int(input("Którą z tych ocen chcesz edytować? "))
            if grade_index > len(self.grade_tables[course]) - 1:
               print("Nie ma oceny o takim indeksie oceny ")
               return
            else:
                newgrade = int(input("Jaką ocena powinna tu trafić? "))
                self.grade_tables[course][grade_index] = newgrade
                print("Oceny po zmianie: ")
                self.display_grades(course)
        else: 
            print("W kursie nie ma ocen. ")
            return

    def display_grades(self, course):
        if self.grade_tables[course]:
            print(f"Wyświetlam oceny z kursu: {course}")
            for index, grade in enumerate(self.grade_tables[course]):
                print(f"Ocena nr {index}: {grade}")      

jan = Student("Jan", "Kowalski", "123456", ["Analiza Matematyczna", "Miernictwo", "Programowanie"])
jan.add_grade((2,3,5), "Miernictwo")
jan.add_grade(3, "Programowanie")
jan.add_grade(5, "Miernictwo")
jan.edit_grade("Miernictwo")
jan.display_grades("Programowanie")

