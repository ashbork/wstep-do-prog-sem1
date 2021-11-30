from moj_modul import Admin as adm
# from moj_modul import Użytkownik as usr

# dwa inne sposoby importu:
# import moj_modul
# from moj_modul import *

# alias na całym module:
# import moj_modul as admin_uzytk


# Python samodzielnie importuje wszystkie potrzebne elementy, nawet jeśli poprosimy go tylko o kl. Admin. Jednakże
# mimo, że klasy Przywileje i Użytkownik są 'częścią' klasy Admin (pierwszy przez użycie instancji tej klasy jako atrybutu, 
# drugi przez dziedziczenie po klasie), nie możemy wywołać ich po tylko tym imporcie. 
# Dlatego poniższa linijka nie zadziała.
# przyw = Przywileje()
# Mimo to, gdy zimportujemy kl. Użytkownik możemy wyraźnie zobaczyć, że Admin dalej, z racji dziedziczenia, jest też Użytkownikiem.

kowalski = adm("Jan", "Kowalski", 28, "Polska", "Abcdefg", ["addpost", "delpost"])
kowalski.opisz_uzytkownika()
kowalski.pozdrow_uzytkownika()
kowalski.wyswietl_przywileje()
# print(dir(adm))
# print(isinstance(kowalski, usr))