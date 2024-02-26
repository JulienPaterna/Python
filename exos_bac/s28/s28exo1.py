def moyenne (tab):
    sum = 0
    for elem in tab:
        sum += elem
    return sum / len(tab)


assert moyenne([1]) == 1
assert moyenne([1, 2, 3, 4, 5, 6, 7]) == 4
assert moyenne([1, 2]) == 1.5

