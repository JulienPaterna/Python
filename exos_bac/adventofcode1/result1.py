import sys

with open(sys.argv[1]) as f:
    fichier = f.read()

def adding(fichier):
    tab = fichier.split("\n")
    num_tab = []
    tot = 0
    for elem in tab:
        num_tab = []
        for char in elem:
            if char.isnumeric() == True:
                num_tab.append(char)
        if len(num_tab) == 1:
            tot += int(num_tab[0]+num_tab[0])
        elif(len(num_tab) > 1):
            tot += int(num_tab[0]+num_tab[len(num_tab) - 1])
    return tot

print(adding(fichier))