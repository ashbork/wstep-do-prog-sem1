class Prostokat:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def pole(self):
        return self.a * self.b
    
    def wymiary(self):
        return f"Ten prostokąt ma wymiary {self.a} x {self.b}." 

# Klasa Kwadrat dziedziczy metodę pole bez żadnych zmian. By nie spowodować błędu wynikającego z braku atrybutu 'b' w klasie Kwadrat nadpisałem metodę __init__,
# tworząc atrybut 'b' i zapisując go jako równy 'a'.
class Kwadrat(Prostokat):
    def __init__(self, a):
        self.a = self.b = a


rect = Prostokat(3, 10)
print(rect.pole())
print(rect.wymiary())
sqr = Kwadrat(8)
print(sqr.pole())
print(sqr.wymiary())