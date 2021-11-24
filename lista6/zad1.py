import datetime


class Restauracja:
    """
    Klasa Restauracja przechowuje dane nt. danej restauracji.
    Atrybuty:
    nazwa (str): nazwa restauracji
    typ (str): typ restauracji ('kuchnia')
    klienci (int) -> 0: liczba obsłużonych klientów
    godziny (tuple(int, int)): godziny otwarcia restauracji (od godz. [0] do godz. [1]). Jeśli są równe, restaurację
    uznajemy za całodobową.
    """
    def __init__(self, nazwa, typ, godziny):
        self.nazwa = nazwa
        self.typ = typ
        self.klienci = 0
        # podanie równych godzin sprawi, że restauracja będzie "całodobowa"
        # (spokojnie, pracownicy mają płacone podwójnie za nocki)
        self.godziny = (min(godziny), max(godziny))
        self.calodobowa = False if not min(godziny) == max(godziny) else True

    def opis_restauracji(self):
        # Zwraca nazwę restauracji, typ restauracji i liczbę klientów
        print(f"Restauracja {self.nazwa} typu {self.typ} serwuje jedzenie {self.klienci} klientom.")

    def ustaw_liczbe_obsluzonych_klientow(self, nowa):
        # Zmienia liczbę klientów na argument nowa (int), jeśli jest nieujemny
        if isinstance(nowa, int) and nowa >= 0:
            print(f"Przed zmianą {self.nazwa} miała {self.klienci} klientów. Zmieniam na {nowa}.")
            self.klienci = nowa
        else:
            print("Ta metoda przyjmuje tylko nieujemne liczby całkowite (int).")

    def dodaj_liczbe_obsluzonych_klientow(self, do_dodania):
        # Dodaje wartość do_dodaia do obecnej liczby obsłużonych klientów, jeśli do_dodania jest intem i ta operacja
        # nie wywołuje ujemnej liczby klientów
        if isinstance(do_dodania, int) and (self.klienci + do_dodania) >= 0:
            print(f"Przed dodaniem/odjęciem klientów restauracja miała {self.klienci} klientów."
                  f" Zmieniam na {self.klienci + do_dodania}.")
        else:
            print("Podano nieprawidłowy argument lub ta operacja spowodowałaby ujemną liczbę klientów")
            
    def czy_otwarta(self):
        # Sprawdza, czy restauracja jest całodobowa. Jeśli jest, pokazuje że jest otwarta. Jeśli nie jest, sprawdza
        # obecną godzinę i porównuje ją z godzinami otwarcia pod atrybutem godziny. Zwraca odpowiedź i obecną godzinę.
        if self.calodobowa:
            print("Restauracja pracuje całą dobę, teraz jest otwarta.")
        else:
            teraz = datetime.datetime.now()
            if self.godziny[0] < teraz.hour < self.godziny[1]:
                print(f"Restauracja pracuje od godziny {self.godziny[0]} do {self.godziny[1]},"
                      f"teraz jest otwarta ({teraz.strftime('%H:%M')}).")
            else:
                print(f"Restauracja pracuje od godziny {self.godziny[0]} do {self.godziny[1]}, "
                      f"teraz jest zamknięta ({teraz.strftime('%H:%M')}).")


class Lodziarnia(Restauracja):
    """
    Klasa Lodziarnia jest podrzędną kl. Restauracja i oprócz atrybutów i metod swojej nadrzędnej przechowuje dostępne
    smaki.
    Atrybuty:
    nazwa (str): nazwa restauracji
    typ (str): typ restauracji ('kuchnia')
    klienci (int) -> 0: liczba obsłużonych klientów
    godziny (tuple(int, int)): godziny otwarcia restauracji (od godz. [0] do godz. [1]). Jeśli są równe, restaurację
    uznajemy za całodobową.
    smaki (list): smaki dostępne w restauracji
    """
    def __init__(self, nazwa, godziny, smaki=None):
        """Użycie smaki=[] jest błędem - ta wartość jest deklarowana przy definicji funkcji, nie przy każdym wywołaniu.
        Przez to moglibyśmy nadpisać domyślną wartość i zmienić ją dla kolejnych instancji klasy. Stąd domyślne None."""
        super().__init__(nazwa, "Lodziarnia", godziny)
        self.smaki = [] if smaki is None else smaki

    def wyswietl_smaki(self):
        # Jeśli smaki nie jest puste, zwraca wszystkie elementy razem z ich indeksami.
        if self.smaki:
            print(f"W lodziarni {self.nazwa} występują smaki:")
            for index, smak in enumerate(self.smaki):
                print((index+1), smak)
        else:
            print(f"W lodziarni {self.nazwa} skończyły się lody :(")


nadmorska = Restauracja("Nadmorska", "Śródziemnomorska", (12, 18))
nadmorska.opis_restauracji()
nadmorska.ustaw_liczbe_obsluzonych_klientow(5)
nadmorska.dodaj_liczbe_obsluzonych_klientow(50)
nadmorska.dodaj_liczbe_obsluzonych_klientow(-60)
nadmorska.czy_otwarta()

messina = Restauracja("Messina", "Włoska", (0, 0))
messina.czy_otwarta()

przelam_lody = Lodziarnia("Przełam Lody", (10, 20), ["Czekoladowe", "Śmietankowe", "Waniliowe", "Sorbet jabłkowy"])
przelam_lody.wyswietl_smaki()
przelam_lody.opis_restauracji()
nadmorska.ustaw_liczbe_obsluzonych_klientow(10)
nadmorska.dodaj_liczbe_obsluzonych_klientow(-5)

wanilia = Lodziarnia("Wanilia", (16, 24))
wanilia.wyswietl_smaki()
