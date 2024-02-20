def verifie(tab) : 
    n = len(tab)
    if n == 0 : 
        return "tableau vide"
    for i in range(n - 1): # range => part de 0 et va jusqu'à "n-1" sans l'atteindre
        if tab[i] > tab[i + 1] : 
            return False
    return True
