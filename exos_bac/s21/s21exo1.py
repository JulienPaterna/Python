def delta(tab):
    result = [tab[0]]
    for i in range(1, len(tab)):
        result.append(tab[i] - tab[i - 1])
    return result



print(delta([1000, 800, 802, 1000, 1003, 0]))
print(delta([42]))