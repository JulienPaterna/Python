# def binaire(a):
#     bin_a = str(...)
#     a = a // 2
#     while a ... :
#         bin_a = ...(a%2) + ...
#         a = ...
#     return bin_a


def binaire(a): 
    reste = str(a%2)
    a = a // 2
    while a > 0:
        reste = str(a%2)+reste
        a = a // 2
    return reste


print(binaire(0))
#'0'
print(binaire(77))
#'1001101'