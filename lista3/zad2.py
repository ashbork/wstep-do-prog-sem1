import sys
import math

A, B, C = 3, 2, -5
# sprawdzamy, czy funkcja jest kwadratowa
if A == 0:
    print("Funkcja nie jest funkcją kwadratową")
    sys.exit()
# kalkulacja wartości delta
delta = B**2 - 4 * (A * C)
if delta >= 0:
    x1 = (-B + math.sqrt(delta))/(2 * A)
    x2 = (-B - math.sqrt(delta))/(2 * A)
    if x1 == x2:
        print("Rozwiązaniem jest {x1}")
    else:
        print(f"Rozwiązania to {x1:.2f} oraz {x2:.2f}.")
else:
    print("Funkcja nie ma rzeczywistych rozwiązań.")
