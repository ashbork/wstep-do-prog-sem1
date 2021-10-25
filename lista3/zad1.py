# zad.1 (w 3.10 użyłbym match case statement)
wiek_uzytkownika = int(input("Podaj wiek widza:"))
if wiek_uzytkownika < 0:
    print("Niewłaściwy wiek.")
    cena = -1
elif wiek_uzytkownika < 16:
    cena = 2.99
elif wiek_uzytkownika < 64:
    cena = 5.99
else:
    cena = 4.99
print(cena)
