def taille(arbre, lettre):
    if lettre == '':
        return 0
    else:
        return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])
     


a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], 'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], 'H':['','']}

print(taille(a, 'F'))
#9