def liste_puissances(a, n):
    result = [a]
    puissance = a
    for i in range (1, n):
        puissance *= a
        result.append(puissance)
    return result



def liste_puissances_borne(a, borne):
    if (a < 2):
        return ('a doit être supérieur ou égal à 2')
    result = []
    n = 1
    while liste_puissances(a, n)[-1] < borne:
        result = liste_puissances(a, n)
        n += 1
    return result

print(liste_puissances(3, 5))
print(liste_puissances(-2, 4))
print(liste_puissances_borne(2, 16))
print(liste_puissances_borne(2, 17))
print(liste_puissances_borne(5, 5))
print(liste_puissances_borne(1, 5))