import glob

def find_start_login (tab):
    for i in range(len(tab[0])):
        for j in range(1, len(tab)):
            if tab[j][i] != tab[0][i]:
                start_login = i
                return start_login

pdfs = glob.glob("./all_pdf/*.pdf")
pdf_tab = []
for pdf in pdfs:
    pdf_tab.append(pdf)

def find_end_login(tab):
    for i in range(1, len(tab[0])):
        for j in range(1, len(tab)):
            if tab[j][len(tab[j]) - i] != tab[0][len(tab[0]) - i]:
                end_login = i 
                return end_login

s = find_start_login(pdf_tab)
e = find_end_login(pdf_tab)
login_tab = []

for elem in pdf_tab:
    login_tab.append(elem[s:-(e-1)])

with open("logins.txt", "w") as file:
    file.write(login_tab[0] + "\n")

for i in range(1, len(login_tab)):
    with open("logins.txt", "a") as file:
        file.write(login_tab[i] + "\n") 
