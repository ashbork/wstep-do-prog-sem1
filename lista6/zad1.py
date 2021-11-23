import datetime


class Restauracja:    
    def __init__(self, nazwa, typ, godziny):
        self.nazwa = nazwa
        self.typ = typ
        self.klienci = 0
        # podanie równych godzin sprawi, że restauracja będzie "całodobowa"
        # (spokojnie, pracownicy mają płacone podwójnie za nocki)
        self.godziny = (min(godziny), max(godziny))

    def opis_restauracji(self):
        print(f"Restauracja {self.nazwa} typu {self.typ} serwuje jedzenie {self.klienci} klientom.")

    def ustaw_liczbe_obsluzonych_klientow(self, nowa):
        if isinstance(nowa, int) and nowa >= 0:
            print(f"Przed zmianą {self.nazwa} miała {self.klienci} klientów. Zmieniam na {nowa}.")
            self.klienci = nowa
        else:
            print("Ta metoda przyjmuje tylko nieujemne liczby całkowite (int).")

    def dodaj_liczbe_obsluzonych_klientow(self, do_dodania):
        if isinstance(do_dodania, int) and (self.klienci + do_dodania) >= 0:
            print(f"Przed dodaniem/odjęciem klientów restauracja miała {self.klienci} klientów."
                  f" Zmieniam na {self.klienci + do_dodania}.")
        else:
            print("Podano nieprawidłowy argument lub ta operacja spowodowałaby ujemną liczbę klientów")
            
    def czy_otwarta(self):
        teraz = datetime.datetime.now()
        if self.godziny[0] == self.godziny[1]:
            print("Restauracja pracuje całą dobę, teraz jest otwarta.")
        else:
            if self.godziny[0] < teraz.hour < self.godziny[1]:
                print(f"Restauracja pracuje od godziny {self.godziny[0]} do {self.godziny[1]},"
                      f"teraz jest otwarta ({str(teraz.tm_hour) + ':' + str(teraz.tm_min)}).")
            else:
                print(f"Restauracja pracuje od godziny {self.godziny[0]} do {self.godziny[1]}, "
                      f"teraz jest zamknięta ({teraz.strftime('%H:%M')}).")


class Lodziarnia(Restauracja):
    def __init__(self, nazwa, godziny, smaki = []):
        super().__init__(nazwa, "Lodziarnia", godziny)
        self.smaki = smaki
    def wyswietl_smaki(self):
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

messina = Restauracja("Messina", "Włoska", (0,0))
messina.czy_otwarta()

przelam_lody = Lodziarnia("Przełam Lody", (10, 20), ["Czekoladowe", "Śmietankowe", "Waniliowe", "Sorbet jabłkowy"])
przelam_lody.wyswietl_smaki()
przelam_lody.opis_restauracji()
nadmorska.ustaw_liczbe_obsluzonych_klientow(10)
nadmorska.dodaj_liczbe_obsluzonych_klientow(-5)

wanilia = Lodziarnia("Wanilia", (16, 24))
wanilia.wyswietl_smaki()
