def solution_dynamique(tab):
    gains=[]
    n = len(tab)
    for ligne in range(n):
        gains.append([])
        for colonne in range(ligne+1):
            gains[ligne].append(tab[ligne][colonne])
    for ligne in range(n-2,-1,-1):
        for colonne in range(ligne+1):
            gains[ligne][colonne]= tab[ligne][colonne] + max(gains[ligne+1][colonne],
                            gains[ligne+1][colonne+1])
    return gains[0][0]


tab=[[5],
     [8,10],
     [11,3,4],
     [6,10,7,12]]