def nb_repetitions(elt, tab):
    nb_rep = 0
    for elem in tab:
        if elem == elt:
            nb_rep += 1
    return nb_rep



print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))
#3
print(nb_repetitions('A', [ 'B', 'A', 'B', 'A', 'R']))
#2
print(nb_repetitions(12, [1, '! ', 7, 21, 36, 44]))
#0
print(nb_repetitions('w', [12, 'R', 19, 'w']))