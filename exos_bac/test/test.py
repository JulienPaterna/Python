tab = ['a', 'b', 'c', 'd']
tab1 = list(tab)

# print(tab, tab1)

x = tab1.pop()
# print(x)
# print(tab1)

tupl1 = ('ok', 'coucou')
tupl2 = ('salut', 'hello')
tupl3 = ('yo', 'hye')
tupl = (tupl1, tupl2, tupl3)
# print(tupl[1][1])
# print(tupl[1][1])

L = [[0 for i in range(4)] for i in range(6)]
# print(L)

tab1 = [4, 0, 1, 3]
tab2 = [4, 5, 6, 7]
# print(tab1 + tab2)
# print(tab2[2:])
# print(tab2[1:3])
# print(tab2[:4])

tab = {'Bob': 102, 'Ada': 201, 'Alice': 103, 'Tim': 50}
# for nom, value in tab.items():
#     print(nom, ":", value)
    
txt = ['hello', 'salut']
tab = []

for elem in txt:
    x = list(elem)
    tab.append(x)

# print(tab)

a = (1, 3)
# print(a)

boites = [0]*3
# print(boites)

boites = [4, 2, 3]
boites = boites[1:]
# print(boites)

str = 'hello'
result = 'a'
# print(str+result)

# dico = {'hello', 'salut'}
# if 'salut' in dico:
#     print(True)
# else:
#     print(False)

# print('A' < 'B')

a = {1: 5, 2: 7}
b = {2: 4, 5: 3, 8: 2}
c = {}
for elem_a in a:
    c[elem_a] = a[elem_a]
for elem_b in  b:
    c[elem_b] = b[elem_b]
# print(max(len(a), len(b)))
    
from random import randint
# print(randint(1,3))

animaux = [ {'nom':'Medor', 'espece':'chien', 'age':5, 'enclos':2},
 {'nom':'Titine', 'espece':'chat', 'age':2, 'enclos':5},
 {'nom':'Tom', 'espece':'chat', 'age':7, 'enclos':4},
 {'nom':'Belle', 'espece':'chien', 'age':6, 'enclos':3},
 {'nom':'Mirza', 'espece':'chat', 'age':6, 'enclos':5}]
# print(animaux[0]['nom'])

a = {}
a['salut'] = 'hello'
# print(a)

tab = []
tab.append(1)
# print(tab)

#argecho.py
# import sys
# test = sys.argv[1]

# print(test)
# for arg in sys.argv: 
#     print(arg)

# try:
#   with open("text.tx", 'r') as fichier:
#     fichier = fichier.read()
#     print(fichier)
# except:
#   print("Files doesn't exist")


map = {}
keys = ['a', 'b', 'c', 'a', 'a', 'c']

for letter in keys:
    try: 
        value = map[letter]
        value += 1
        map.update({letter: value})
    except:
        map.update({letter: 1})
# map.update({'a': 1})
# print(map)

n = 3
liste = [['O']*n]*n
# print(liste)

result = []
result.extend((1, 2))
print(result)