def ajoute_dictionnaires(d1,d2):
    d = {}
    for elem_d1 in d1:
        d[elem_d1] = d1[elem_d1]
    for elem_d2 in d2:
        if elem_d2 in d:
            d[elem_d2] = d[elem_d2] + d2[elem_d2]
        else:
            d[elem_d2] = d2[elem_d2]            
    return dict(sorted(d.items()))




