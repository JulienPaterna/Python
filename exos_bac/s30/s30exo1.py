def moyenne(liste):
    result = 0
    for nbr in liste:
        result += nbr
    return result/len(liste)



print(moyenne([1.0]))
#1.0
print(moyenne([1.0, 2.0, 4.0]))
#2.3333333333333335