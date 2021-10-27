
def price_by_age(age):   
    try: 
        if age <= 0:
            return(-1)
        elif age < 16:
            return(2.99)
        elif age < 64:
            return(5.99)
        else:
            return(4.99)
    except TypeError:
        return(-1)

argument = int(input("Podaj wiek widza: "))
print(price_by_age(argument))

