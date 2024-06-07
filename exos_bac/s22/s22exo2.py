dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}


# def est_parfait(mot):
#     concat = []
#     addit = 0
#     boolean = False
#     for elem in mot:
#         concat.append(str(dico[elem]))
#         addit += dico[elem]
#     alpha = int(''.join(concat))
#     if ((alpha % addit) == 0): 
#         boolean = True
#     return addit, alpha, boolean

def est_parfait(mot):
    code_concatene = ""
    code_additionne = 0
    for c in mot:
        code_concatene = code_concatene + str(dico[c])
        code_additionne = code_additionne + dico[c]
    code_concatene = int(code_concatene)
    if code_concatene%code_additionne == 0 :
        mot_est_parfait = True
    else:
        mot_est_parfait = False
    return code_additionne, code_concatene, mot_est_parfait

print(est_parfait("PAUL"))
#(50, 1612112, False)
print(est_parfait("ALAIN"))
#(37, 1121914, True)
