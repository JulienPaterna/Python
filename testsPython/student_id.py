import sys

with open(sys.argv[1]) as F:
    fichier = F.read()

students = fichier.split('\n')

request_tab = []
for student in students:
    names = student.split(' ')
    student_lastname = []
    student_firstname = []
    for elem in names:
        if ord(elem[1]) >= 65 and ord(elem[1]) <= 90:
            student_lastname.append(elem)
        else:
            student_firstname.append(elem)
    studentLastname = " ".join(student_lastname)
    studentFirstname = " ".join(student_firstname)
    student = '(lastname = \''+studentLastname+'\''+' AND firstname = \''+studentFirstname+'\')'
    request_tab.append(student)

students_request = " or ".join(request_tab)
request = 'SELECT id  FROM reen_student \nWHERE '+students_request
print(request)