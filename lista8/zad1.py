with open("zad1.txt", "a") as working_file:
    while (to_add := input("Podaj kolejną linijkę, lub wciśnij enter, by przestać dodawać kolejne\n")) != "":
        working_file.write(to_add+"\n")
