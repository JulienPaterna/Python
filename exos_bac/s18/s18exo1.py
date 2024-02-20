def max_et_indice(tab):
    indice = len(tab) - 1
    i = indice
    max = tab[i]
    if (len(tab) == 1):
        return max, i
    else:
        while (i >= 0):
            if (tab[i] >= max):
                max = tab[i]
                indice = i
            i -= 1
        
        return max, indice





print(max_et_indice([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]))
print(max_et_indice([-2]))
print(max_et_indice([-1, -1, 3, 3, 3]))
print(max_et_indice([1, 1, 1, 1]))
