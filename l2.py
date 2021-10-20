# zad. 1, przypisanie wartości 12.5 do zmiennej "zmienna"
zmienna = 12.5
print("Przypisana wartość: zmienna")
# zad. 2 przy pomocy fstringów (użyta zmienna z 1)
print(f"\nDodawanie: {2+zmienna} \nOdejmowanie: {3-1} \nMnożenie: {0.5*4} \nDzielenie: {12/3} \nModulo (reszta z dzielenia): {13%3}")
# zad. 3
liczbowy_calkowity = int(13)
lancuch_znakow = str(liczbowy_calkowity)
string_na_int = float(lancuch_znakow)
print(liczbowy_calkowity, lancuch_znakow, string_na_int)
# zad. 4, dane osobowe zapisane na liście, wyprintowane przez fstring i z użyciem metod klasy string 
dane_osobowe = ["ab", "adam", "błoński"]
str_dane = (f"\nInicjały: {dane_osobowe[0].upper()}\nImię: {dane_osobowe[1].capitalize()}\nNazwisko: {dane_osobowe[2].capitalize()}")
print(str_dane)
