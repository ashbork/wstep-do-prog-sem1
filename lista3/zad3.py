def avg(*numbers):
    try:
        average = sum(numbers)/len(numbers)
        parity = "parzysta" if int(average)%2 == 0 else "nieparzysta"
        print(f"Średnia podanych liczb to {average}. Po konwersji na liczbę całkowitą otrzymujemy {int(average)}, jest to liczba {parity}.\n")
    except TypeError:
        print(f"Podane argumenty, {numbers}, są nieprawidłowego typu.\n")

avg(1,2,3,4)
avg(100, -10, 30)
avg("nie jestem liczbą", 2, 3)
