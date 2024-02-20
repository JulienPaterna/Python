class ABR:
    def __init__(self, g, c, d):
        self.gauche = g
        self.cle = c
        self.droite = d

    def __repr__(self):
        return f"({self.gauche}, {self.cle}, {self.droite})"
    

n0 = ABR(None, 0, None)
n3 = ABR(None, 3, None)
n2 = ABR(None, 2, n3)
abr1 = ABR(n0, 1, n2)

def ajoute(cle, a):
    if a == None: 
        return ABR(None, cle, None)
    elif cle == a.cle:
        return a
    elif cle < a.cle:
        return ABR(ajoute(cle, a.gauche), a.cle, a.droite)
    elif cle > a.cle:
        return ABR(a.gauche, a.cle, ajoute(cle, a.droite))


print(ajoute(4, abr1))
print(ajoute(-5, abr1))
print(ajoute(2, abr1))
