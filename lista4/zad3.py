karton_mleka = {
    "data_waznosci": (1, 12, 2021),
    "pojemnosc_w_litrach": 1,
    "cena": 3.99,
    "marka": "Mlekpol"
}
print(karton_mleka["data_waznosci"])
print(karton_mleka["pojemnosc_w_litrach"])
print(karton_mleka["cena"])
print(karton_mleka["marka"])
print(f"Cena sześciu kartonów mleka wynosi {6 * karton_mleka['cena']}")
