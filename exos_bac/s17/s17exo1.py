def moyenne(liste_notes):
    total_note_coef = 0
    total_coef = 0
    for elem in liste_notes:
        note, coef = elem
        total_note_coef += note * coef
        total_coef += coef
        # total_note_coef += elem[0] * elem[1]
        # total_coef += elem[1]
    return total_note_coef / total_coef



print(moyenne([(15, 2), (9, 1), (12, 3)]))
