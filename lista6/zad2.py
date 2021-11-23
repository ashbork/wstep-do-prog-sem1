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

jan_kowalski = Użytkownik("Jan", "Kowalski", 15, "Polska", "Qwertyuiopas")
jan_kowalski.opisz_uzytkownika()
jan_kowalski.logowanie("wlamuje ci sie na kontoo")
jan_kowalski.opisz_uzytkownika()
jan_kowalski.logowanie("nie ukrywam, troche trudno to zrobic")
jan_kowalski.opisz_uzytkownika()
jan_kowalski.logowanie("przez zaimplementowane zabezpieczenia")
try:
    print(jan_kowalski.__haslo, jan_kowalski.__cryptokey)
except AttributeError:
    print("Hasło i klucz szyfrowania są prywatnymi atrybutami!")
jan_kowalski.opisz_uzytkownika()
jan_kowalski.logowanie("Qwertyuiopas")
jan_kowalski.opisz_uzytkownika()

thomas_anderson = Admin("Thomas", "Anderson", 36, "USA", "matrix12345", ["addpost", "removepost", "editpost", "banusr", "timeoutusr", "adminpanel"])
thomas_anderson.wyswietl_przywileje()
