class Arbre:
    def __init__(self, etiquette):
        self.v = etiquette
        self.fg = None
        self.fd = None

def parcours(arbre, liste):
    if arbre != None:
        parcours(arbre.fg, liste)
        liste.append(arbre.v)
        parcours(arbre.fd, liste)
    return liste

def insere(arbre, cle):
    """ arbre est une instance de la classe Arbre qui implémente un arbre binaire de recherche."""
    if cle < arbre.v:
        if arbre.fg != None:
            insere(arbre.fg, cle)
        else:
            arbre.fg = Arbre(cle)
    else:
        if arbre.fd != None:
            insere(arbre.fd, cle)
        else:
            arbre.fd = Arbre(cle)


Abr = Arbre(5)
abr1 = Arbre(2)
abr2 = Arbre(3)
abr3 = Arbre(7)

Abr.fg = abr1
Abr.fd = abr3
Abr.fg.fd = abr2

insere(Abr, 1)
insere(Abr, 4)
insere(Abr, 6)
insere(Abr, 8)

print(parcours(Abr, []))