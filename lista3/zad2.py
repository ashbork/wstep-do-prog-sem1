import math


def roots(a, b, c):
    try:
        if a == 0:
            print("Funkcja nie jest f kwadratową (a = 0)")
            return
        delta = b ** 2 - 4 * (a * c)
        if delta == 0:
            return -b / (2 * a)
        elif delta > 0:
            return [(-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)]
        else:
            return "Brak miejsc zerowych"
    except TypeError:
        return "Nieprawidłowe argumenty"


try:
    print(roots(1, 2, 1))
    print(roots(1, "a", 1))
    print(roots(3, 2, 1))
    print(roots(-1, 0, 0))
    print(roots())
except TypeError:
    print("Nieprawidłowe argumenty w jednej z wywołanych funkcji")
    exit(1)
