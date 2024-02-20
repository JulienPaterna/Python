def nbLig(image):
    #'''renvoie le nombre de lignes de l'image'''
    # print(len(image))
    return len(image)

def nbCol(image):
    #'''renvoie la largeur de l'image'''
    # print(len(image[0]))
    return len(image[0])

def negatif(image):
    # print(image)
    #'''renvoie le négatif de l'image sous la forme d'une liste de listes'''
    # on créé une image de 0 aux mêmes dimensions que le paramètre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]
    print(L)
    return L

def binaire(image, seuil):
    #'''renvoie une image binarisée de l'image sous la forme d'une liste de listes contenant des 0 si la valeur 
    #du pixel est strictement inférieure au seuil et 1 sinon'''
    # on crée une image de 0 aux mêmes dimensions que le paramètre image
    L = [[0 for l in range(nbCol(image))] for h in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil :
                L[i][j] = 0
            else:
                L[i][j] = 1
    print(L)
    return L


image = [[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
negatif(image)
binaire(image, 120)
