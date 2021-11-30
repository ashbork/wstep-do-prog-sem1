from cryptography.fernet import Fernet 


class Uzytkownik:
    """
    Klasa Użytkownik przechowuje informacje nt. użytkownika i odpowiada za próby logowania na jego konto.
    Atrybuty:
    imie (str), nazwisko (str), wiek (int), kraj (str): dane użytkownika
    __cryptokey (bytes): klucz kryptograficzny użytkownika, prywatny atrybut
    __haslo (bytes): zaszyfrowane hasło użytkownika, prywatny atrybut
    proby (int): próby zalogowania na konto użytkownika
    """
    def __init__(self, imie, nazwisko, wiek, kraj, haslo):
        """Konstruktor klasy przyjmuje dane użytkownika, dodatkowo generuje mu klucz kryptograficzny
        i szyfruje przy jego pomocy hasło (przechowywanie go w plaintext to zła praktyka)"""
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
        self.kraj = kraj
        self.__cryptokey = Fernet.generate_key()
        self.__haslo = Fernet(self.__cryptokey).encrypt(haslo.encode('ascii'))
        self.proby = 0

    def opisz_uzytkownika(self):
        """Opisuje użytkownika przy pomocy jego atrybutów. Sprawdza też i pokazuje, czy jest administratorem."""
        print(f"Użytkownik {self.imie} {self.nazwisko} z {self.kraj} ma {self.wiek} lat. Próbowano dostać się na ich "
              f"konto bez powodzenia {self.proby} razy. {'Jest' if isinstance(self, Admin) else 'Nie jest'} "
              f"administratorem.\n")
    
    def pozdrow_uzytkownika(self):
        """Pozdrawia użytkownika"""
        print(f"Hej, {self.imie}, miłego dnia!")

    def resetuj_proby_logowania(self):
        """Resetuje próby logowania"""
        self.proby = 0

    def dodaj_probe_logowania(self):
        """Dodaje jedną próbę logowania"""
        self.proby += 1

    def logowanie(self, haslo):
        """Rozszyfrowuje hasło użytkownika i porównuje je z podanym parametrem haslo. Jeśli jest prawidłowe, próby
        logowania są zresetowane (prawdziwy właściciel konta się 'zalogował').
        Jeśli nie jest, dodaje próbę logowania."""
        if haslo.encode('ascii') == Fernet(self.__cryptokey).decrypt(self.__haslo):
            print("Wpisano poprawne hasło, zresetowano próby logowania\n")
            self.resetuj_proby_logowania()
        else:
            print("Niepoprawne hasło.\n")
            self.dodaj_probe_logowania()


class Admin(Uzytkownik):
    """Dziedziczy po klasie Użytkownik, dodatkowo przyjmuje atrybut przywileje.
    Ten jest nowym obiektem klasy Przywileje
    Atrybuty:
    imie (str), nazwisko (str), wiek (int), kraj (str): dane użytkownika
    __cryptokey (bytes): klucz kryptograficzny użytkownika, prywatny atrybut
    __haslo (bytes): zaszyfrowane hasło użytkownika, prywatny atrybut
    proby (int): próby zalogowania na konto użytkownika
    przywileje (Przywileje): przywileje"""
    def __init__(self, imie, nazwisko, wiek, kraj, haslo, przywileje):
        super().__init__(imie, nazwisko, wiek, kraj, haslo)
        self.przywileje = Przywileje(przywileje)

    def wyswietl_przywileje(self):
        """Wyświetla przywileje administratora, jeśli są."""
        if self.przywileje.lst:
            print("Przywileje administratora:")
            for index, priv in enumerate(self.przywileje.lst):
                print(index+1, priv)
        else:
            print(f"Administrator {self.imie} nie ma żadnych przywilejów")


class Przywileje:
    """Obiekt przechowuje listę przywilejów administratora.
    Atrybuty:
    lst (list): lista przywilejów administratora"""
    def __init__(self, przywilej=None):
        self.lst = przywilej if przywilej is not None else []


jan_kowalski = Uzytkownik("Jan", "Kowalski", 15, "Polska", "Qwertyuiopas")
jan_kowalski.opisz_uzytkownika()
jan_kowalski.logowanie("wlamuje ci sie na kontoo")
jan_kowalski.opisz_uzytkownika()
jan_kowalski.logowanie("nie ukrywam, troche trudno to zrobic")
jan_kowalski.opisz_uzytkownika()
jan_kowalski.logowanie("przez zaimplementowane zabezpieczenia")

# Ewidentnie, to nie zadziała
# zaszyfrowanie hasła i ustawienie go jako atr. pryw. utrudni zdobycie go przez np. code injection
try:
    print(jan_kowalski.__haslo, jan_kowalski.__cryptokey)
except AttributeError:
    print("Hasło i klucz szyfrowania są prywatnymi atrybutami!")

jan_kowalski.opisz_uzytkownika()
jan_kowalski.logowanie("Qwertyuiopas")
jan_kowalski.opisz_uzytkownika()

thomas_anderson = Admin("Thomas", "Anderson", 36, "USA", "matrix12345", ["addpost", "removepost", "editpost",
                                                                         "banusr", "timeoutusr", "adminpanel"])
thomas_anderson.wyswietl_przywileje()
thomas_anderson.opisz_uzytkownika()
