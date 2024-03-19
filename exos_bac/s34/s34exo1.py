def moyenne(tab):
    if len(tab) != 0:
        sum = 0
        for num in tab:
            sum += num
        return sum / len(tab)
    else: 
        return 'pour avoir la moyenne de quelque chose, il faut avoir quelque chose!!!' 
    
print(moyenne([5, 3, 8]))
#5.333333333333333
print(moyenne([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#5.5
print(moyenne([]))