def empaqueter(liste_masses, c):
    if (liste_masses == [] or liste_masses == [0]):
        return 0
    boites = [liste_masses[0]]
    liste_masses = liste_masses[1:]
    for masse in liste_masses: 
        i = 0
        while (i <= len(boites) - 1 and boites[i] + masse > c):
            i += 1
        if (i < len(boites)):
            boites[i] += masse
        else: 
            boites.append(masse)
    return len(boites) 


print(empaqueter([7, 6, 3, 4, 8, 5, 9, 2], 11))
print(empaqueter([1, 5, 2], 5))
print(empaqueter([1, 5, 2, 4, 3], 5))
print(empaqueter([1, 5, 2, 6, 2], 7))
print(empaqueter([], 7))
print(empaqueter([0], 7))
