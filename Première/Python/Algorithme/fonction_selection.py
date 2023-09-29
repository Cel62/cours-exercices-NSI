def indice_mini(liste, indice_depart):
    minimum = liste[indice_depart]
    indice_minimum = indice_depart
    for i in range(indice_depart + 1, len(liste)):
        if liste[i] < minimum:
            minimum = liste[i]
            indice_minimum = i
    return indice_minimum

def tri_selection(liste):
    for i in range(len(liste)):
        indice_minimum = indice_mini(liste, i)
        liste[i],liste[indice_minimum] = liste[indice_minimum],liste[i]
    return liste

import doctest
doctest.testmod(verbose=True)