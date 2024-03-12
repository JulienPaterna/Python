def min_et_max(tab):
    min = tab[0]
    max = tab[0]
    for elem in tab:
        if elem < min:
            min = elem
        elif elem > max:
            max = elem
    return {'min': min, 'max': max}



print(min_et_max([0, 1, 4, 2, -2, 9, 3, 1, 7, 1]))
#{'min': -2, 'max': 9}
print(min_et_max([0, 1, 2, 3]))
#{'min': 0, 'max': 3}
print(min_et_max([3]))
#{'min': 3, 'max': 3}
print(min_et_max([1, 3, 2, 1, 3]))
#{'min': 1, 'max': 3}
print(min_et_max([-1, -1, -1, -1, -1]))
#{'min': -1, 'max': -1}