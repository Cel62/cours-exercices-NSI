def fusion(tab1, tab2):
    i1 = 0
    i2 = 0
    tab_sortie = []
    while i1 < len(tab1) and i2 < len(tab2):
        if tab1[i1] < tab2[i2]:
            tab_sortie.append(tab1[i1])
            i1 += 1
        else:
            tab_sortie.append(tab2[i2])
            i2 += 1
    if i1 == len(tab1):
        for elements in tab2[i2:]:
            tab_sortie.append(elements)
    else:
        for elements in tab1[i1:]:
            tab_sortie.append(elements)
    return tab_sortie

def tri_fusion(tab):
    n = len(tab)
    if n < 2:
        return tab
    else:
        return fusion(tri_fusion(tab[0:n//2]), tri_fusion(tab[n//2:n]))
    
def min_dpr(tab):
    return tri_fusion(tab)[0]