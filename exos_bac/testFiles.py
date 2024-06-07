# fichier = open("test/text.txt", "r")
# print(fichier.read())
# fichier.close()

# with open("test/text.txt", "w") as f:
#     f.write("coucou")


with open("test/text.txt", "r") as f:
    fichier = f.read()

new = fichier.split('\n')
for word in new:
    tab = []
    for letter in word:
        if not letter in ['@', '$', '§', '!']:
            tab.append(letter)
    new_tab = []
    for elem in tab:
        n = ord(elem) - 1
        elem = chr(n)
        new_tab.append(elem)
    print(''.join(new_tab))
