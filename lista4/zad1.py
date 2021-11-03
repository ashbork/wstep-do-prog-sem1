# rekurencyjna implementacja przesunięcia listy
def scroll_list_recursive(target, steps):
    if steps:
        target.insert(0, target[-1])
        target.pop()
        steps -= 1
        return scroll_list_recursive(target, steps)
    else:
        return target


# iteracyjna implementacja przesunięcia listy
def scroll_list_iterative(target, steps):
    for n in range(steps):
        target.insert(0, target[-1])
        target.pop()
    return target


lista = [1, 2, 3, 4, 5, 6]
scroll_list_iterative(lista, 1)
print(lista)
scroll_list_recursive(lista, 1)
print(lista)
