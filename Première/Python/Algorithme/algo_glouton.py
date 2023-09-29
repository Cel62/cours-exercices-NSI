def banque(montant, somme = [500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01]):
    m = montant
    r = []
    i = 0
    while m != 0:
        if m >= somme[i]:
            r.append(somme[i])
            m = round(m - somme[i], 2)
        else:
            i = i + 1
    return r

def sac_a_dos(poids_max = 30, objets = ["1", "2", "3", "4"], valeurs = [7, 4, 3, 3], poids = [13, 12, 8, 10]):
    valeurs_sur_poids = []
    
    for i in range(len(objets)):
        valeurs_sur_poids.append((round(valeurs[i]/poids[i], 2), i))
    valeurs_sur_poids.sort(reverse=True)
    
    poids_sac = 0
    valeur_sac = 0
    contenu_sac = []
    
    for j in range(len(objets)):
        if poids[valeurs_sur_poids[j][1]] <= poids_max - poids_sac:
            contenu_sac.append(objets[valeurs_sur_poids[j][1]])
            poids_sac += poids[valeurs_sur_poids[j][1]]
            valeur_sac += valeurs[valeurs_sur_poids[j][1]]
    return contenu_sac, valeur_sac, poids_sac