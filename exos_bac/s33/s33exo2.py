def tri_selection(tab):
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(k+1, N):
            if tab[i] < tab[imin] :
                imin = i
        tab[k] , tab[imin] = tab[imin] , tab[k]


liste = [41, 55, 21, 18, 12, 6, 25, 1, 66]
tri_selection(liste)
print(liste)
#[6, 12, 18, 21, 25, 41, 55]