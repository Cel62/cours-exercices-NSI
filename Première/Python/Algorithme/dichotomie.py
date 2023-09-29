def dichotomie(liste, valeur):
    idebut = 0
    ifin = len(liste) - 1
    while idebut < ifin:
        imilieu = (idebut + ifin) // 2
        if liste[imilieu] == valeur:
            return imilieu
        else:
            if liste[imilieu] < valeur:
                idebut = imilieu + 1
            else:
                ifin = imilieu + 1
    if liste[imilieu]