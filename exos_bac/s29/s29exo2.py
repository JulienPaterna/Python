# def ajoute(indice, element, liste):
#     result = []
#     if indice > len(liste):
#         for elem in liste:
#             result.append(elem)
#         result.append(element)
#     else:
#         for i in range(indice):
#             result.append(liste[i])
#         result.append(element)
#         for i in range(indice, len(liste)):
#             result.append(liste[i])
#     return result
    


def ajoute(indice, element, liste):
    nbre_elts = len(liste)
    L = [0 for i in range(nbre_elts + 1)]
    if indice < nbre_elts :
        for i in range(indice):
            L[i] = liste[i]
        L[indice] = element 
        for i in range(indice + 1, nbre_elts + 1):
            L[i] = liste[i - 1]
    else:
        for i in range(nbre_elts):
            L[i] = liste[i]
        L[i + 1] = element
    return L



print(ajoute(1, 4, [7, 8, 9]))
#[7, 4, 8, 9]
print(ajoute(3, 4, [7, 8, 9]))
#[7, 8, 9, 4]
print(ajoute(4, 4, [7, 8, 9]))
#[7, 8, 9, 4]









