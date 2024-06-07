def chercher(tab, n, i, j):
    if i < 0 or j >= len(tab):
        return None
    elif i > j:
        return None
    m = (i + j) // 2 # division entière
    if tab[m] < n:
        return chercher(tab, n, m+1, j)
    elif tab[m] > n:
        return chercher(tab, n, 0, m-1)
    else:
        return m
    
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 10))
print(chercher([1, 5, 6, 6, 9, 12], 7, 0, 5))
print(chercher([1, 5, 6, 6, 9, 12], 9, 0, 5))
print(chercher([1, 5, 5, 6, 9, 12], 6, 0, 5))