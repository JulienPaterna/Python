a = [1, 0, 1, 0, 1, 1, 0, 1]
b = [0, 1, 1, 1, 0, 1, 0, 0]
c = [1, 1, 0, 1]
d = [0, 0, 1, 1]


def ou_exclusif(tab1, tab2):
    result = []
    for i in range(len(tab1)):
        if tab1[i] == tab2[i]:
            result.append(0)
        else:
            result.append(1)
    return result

# def ou_exclusif(t1, t2):
#     n = len(t1)
#     result = t1
#     for i in range(n):
#         if t1[i] == t2[i]:
#             result[i] = 0
#         else :
#             result[i] = 1
#     return result

print(ou_exclusif(a, b))
#[1, 1, 0, 1, 1, 0, 0, 1]
print(ou_exclusif(c, d))
#[1, 1, 1, 0]