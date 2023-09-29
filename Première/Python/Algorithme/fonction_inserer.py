def inserer_element(liste, indice):
    for j in range(indice):
        if liste[indice-j] < liste[indice-j-1]:
            liste[indice-j],liste[indice-j-1] = liste[indice-j-1],liste[indice-j]
    return liste

def tri_insertion(liste):
    for i in range(1, len(liste)):
        inserer_element(liste, i)
    return liste