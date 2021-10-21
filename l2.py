# zad. 1, przypisanie wartości 12.5 do zmiennej "zmienna"
zmienna = 12.5
print(zmienna)
zmienna += 3.2
print(zmienna)


# zad. 2 przy pomocy fstringów (użyta zmienna z 1)
print(f"\nDodawanie: {2+zmienna} \nOdejmowanie: {3-1} \nMnożenie: {0.5*4} \nDzielenie: {12/3}"
      f" \nModulo (reszta z dzielenia): {13%3}\nPotęga: {2**3}")


# zad. 2 przy pomocy % formattingu
print("\nDodawanie: %i\nOdejmowanie %i\nMnożenie %0.2f\nDzielenie %0.4f\nPotęgowanie %0.2E"
      "\nModulo %i\nDzielenie z zaokr. w dół %i" % ((1+2), (2-2), (2.25 * 3), (1/3), (14**20), (50 % 2), (10//3)))


# zad. 3
liczbowy_calkowity = int(13)
lancuch_znakow = str(liczbowy_calkowity)
string_na_float = float(lancuch_znakow)
print(liczbowy_calkowity, lancuch_znakow, "Float z dokładnością do 3 miejsca %0.3f" % string_na_float)


# zad. 4, dane osobowe zapisane na liście, wyprintowane przez fstring i z użyciem metod klasy string
dane_osobowe = ["ab", "adam", "błoński"]
str_dane = (f"\nInicjały: {dane_osobowe[0].upper()}\n"
            f"Imię: {dane_osobowe[1].capitalize()}\nNazwisko: {dane_osobowe[2].capitalize()}")
print(str_dane)
