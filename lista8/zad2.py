liczba = input("Wpisz liczbę. \n")
if not isinstance(liczba, (int, float)):
    raise ValueError("Input must be a number")
print(f"Podałeś liczbę {liczba}")

# alternatywnie:
# try:
#     liczba = float(input("Wpisz liczbę. \n"))
# except ValueError:
#     print("Nieprawidłowa liczba")
