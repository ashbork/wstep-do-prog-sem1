# rekurencyjna przesunięcie listy
def scroll_list(target, steps):
    if steps:
        target.insert(0, target[-1])
        target.pop()
        steps -= 1
        print(target)
        scroll_list(target, steps)


lista = [1, 2, 3, 4, 5, 6]
scroll_list(lista, 5)
