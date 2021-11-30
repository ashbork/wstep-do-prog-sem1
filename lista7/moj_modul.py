from cryptography.fernet import Fernet 

class Użytkownik:
    def __init__(self, imie, nazwisko, wiek, kraj, haslo):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.kraj = kraj
        self.__cryptokey = Fernet.generate_key()
        self.__haslo = Fernet(self.__cryptokey).encrypt(haslo.encode('ascii'))
        self.proby = 0

    def opisz_uzytkownika(self):
        print(f"Użytkownik {self.imie} {self.nazwisko} z {self.kraj} ma {self.wiek} lat. Próbowano dostać się na ich konto bez powodzenia {self.proby} razy.\n")
    
    def pozdrow_uzytkownika(self):
        print(f"Hej, {self.imie}, miłego dnia!")

    def resetuj_proby_logowania(self):
        self.proby = 0

    def dodaj_probe_logowania(self):
        self.proby += 1

    def logowanie(self, haslo):
        if haslo.encode('ascii') == Fernet(self.__cryptokey).decrypt(self.__haslo):
            print("Wpisano poprawne hasło, zresetowano próby logowania\n")
            self.resetuj_proby_logowania()
        else:
            print("Niepoprawne hasło.\n")
            self.dodaj_probe_logowania()

class Admin(Użytkownik):
    def __init__(self, imie, nazwisko, wiek, kraj, haslo, przywileje):
        super().__init__(imie, nazwisko, wiek, kraj, haslo)
        self.przywileje = Przywileje(przywileje)

    def wyswietl_przywileje(self):
        if self.przywileje.lst:
            print("Przywileje administratora:")
            for index, priv in enumerate(self.przywileje.lst):
                print(index+1, priv)
        else:
            print(f"Administrator {self.imie} nie ma żadnych przywilejów")

class Przywileje:
    def __init__(self, przywilej):
        self.lst = przywilej