def multiplication(a, b):
    result = 0
    for i in range(min(abs(a), abs(b))):
        result += max(abs(a), abs(b))
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        result = 0 - result
    print(result)



multiplication(3, 5)
multiplication(-4, 8)
multiplication(-2, 6)
multiplication(-2, 0)
