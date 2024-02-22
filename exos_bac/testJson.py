import json

# # data = {"nom": "Marlangue", "prenom": "Anne"}

# # with open("test/fichier.json", "w") as f:
# #     json.dump(data, f)

with open("test/fichier.json") as f:
    data = json.load(f)


if data['prenom'] == 'Julien':
    print("coucou chérie")
else:
    print("au revoir")

























