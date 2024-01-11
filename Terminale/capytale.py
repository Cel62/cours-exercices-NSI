def verifie(tableau):
    return tableau == sorted(tableau)

# def indices_maxi(tab):
#     maximum = 0
#     emplacement_maximum = []
#     for i in tab:
#         if i >= maximum:
#             maximum = i
#     return (maximum, emplacement_maximum)

def moyenne(liste_valeur_coefficient):
    numerateur = 0
    denominateur = 0
    for couple in liste_valeur_coefficient:
        numerateur += couple[0] * couple[1]
        denominateur += couple[1]
    if denominateur == 0:
        return None
    return numerateur / denominateur

def a_doublon(liste):
    same_number = 0
    for number in range(len(liste)):
        same_number = liste[number]
        if same_number == liste[number - 1] or same_number == liste[number + 1]:
            return True
    return False