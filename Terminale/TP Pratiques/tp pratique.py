def moyenne(tab):
    if len(tab) == 0:
        return "Erreur"
    result = 0
    for i in tab:
        result += i
    return result / len(tab)

def nb_repetitions(elt, tab):
    nombre_element = 0
    for i in tab:
        if i == elt:
            nombre_element += 1
    return nombre_element