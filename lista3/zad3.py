import sys

przyjmowane_liczby = input("Podaj liczby, które chcesz uśrednić. Oddzielaj je przecinkami.\n")
lista_liczb = przyjmowane_liczby.split(",")
if not przyjmowane_liczby:
    sys.exit()
suma = 0
for l in lista_liczb:
    suma += float(l)
srednia = suma / len(lista_liczb)
print(f"Średnia wynosi {srednia}, przetworzona na l. calkowitą wynosi {int(srednia)}")
if int(srednia) % 2 == 0:
    print("Oraz jest parzysta")
else:
    print("Oraz jest nieparzysta")