import subprocess

with open("test.txt", 'r') as tab:
    tab = tab.read()

new_tab = tab.split("\n")

for fichier in new_tab:
    subprocess.run(['python3', fichier])
