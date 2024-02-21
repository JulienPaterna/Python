def multiplication(n1, n2):
    result = 0
    for i in range(0, min(abs(n1), abs(n2))):  
        result += max(abs(n1), abs(n2))
    if (n1 < 0 and n2 < 0) or (n1 > 0 and n2 > 0):
        return result
    else:
        return -(result)
        




print(multiplication(3, 5))
#15
print(multiplication(-4, -8))
#32
print(multiplication(-2, 6))
#-12
print(multiplication(-2, 0))
#0