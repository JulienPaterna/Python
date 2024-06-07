# def recherche(tab, n):
#     i = -1
#     for k in range(len(tab)):
#         if (tab[k] == n):
#             i = k
#     if (i == -1):
#         print(len(tab))
#     else:
#         print(i)

def recherche(tab,n):
    indice = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            indice = i
    print(indice)
    

recherche([5, 3, 1, 1], 1)
recherche([2, 4], 2)
recherche([2, 3, 5, 2, 4], 3)
