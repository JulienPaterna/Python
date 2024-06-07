def est_un_ordre(tab):
    for i in range(1,len(tab) + 1):
        if i not in tab:
            return False
    return True


def nombre_points_rupture(ordre):
    assert est_un_ordre(ordre)
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < (n - 1):
        if (ordre[i + 1] - ordre[i]) not in [-1, 1]: # l'écart n'est pas 1
            nb = nb + 1
        i = i + 1
    if ordre[n - 1] != n: # le dernier n'est pas n
        nb = nb + 1
    return nb


print(est_un_ordre([1, 6, 2, 8, 3, 7]))
print(est_un_ordre([5, 4, 3, 6, 7, 2, 1, 8, 9]))
print(nombre_points_rupture([5, 4, 3, 6, 7, 2, 1, 8, 9]))
print(nombre_points_rupture([1, 2, 3, 4, 5]))
print(nombre_points_rupture([1, 6, 2, 8, 3, 7, 4, 5]))
print(nombre_points_rupture([2, 1, 3, 4]))

