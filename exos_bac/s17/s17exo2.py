def pascal(n):
    triangle= [[1]]
    for k in range(1,n+1):
        ligne_k = [1]
        for i in range(1,k):
            ligne_k.append(triangle[k-1][i-1]+triangle[k-1][i])
        ligne_k.append(triangle[0][0])
        triangle.append(ligne_k)
    return triangle



# print(pascal(4))
# print(pascal(5))
print(pascal(6))
