class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def taille (a):
    if a == None:
        return 0
    else:
        return (1 + taille(a.fg) + taille(a.fd))
    
def hauteur (a):
    if a == None:
        return 0
    else:
        return (1 + max(hauteur(a.fg), hauteur(a.fd)))

a=Arbre(1)
a.fg=Arbre(4)
a.fd=Arbre(0)
a.fd.fd=Arbre(7)

b=Arbre(0)
b.fg=Arbre(1)
b.fg.fg=Arbre(3)
b.fd=Arbre(2)
b.fd.fg=Arbre(4)
b.fd.fd=Arbre(5)
b.fd.fg.fd=Arbre(6)

abr = Arbre(0)
a1 = Arbre(1)
a3 = Arbre(3)
a2 = Arbre(2)
a4 = Arbre(4)
a5 = Arbre(5)
a6 = Arbre(6)

a4.fd = a6
a2.fg = a4
a2.fd = a5
a1.fg = a3
abr.fg = a1
abr.fd = a2

print(taille(a))
print(taille(abr))
print(hauteur(a))
print(hauteur(abr))