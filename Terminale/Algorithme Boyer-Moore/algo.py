from random import randint

NO_CAR = 256

def recherche(txt, motif):
    m = len(motif)
    n = len(txt)
    tab_car = [-1] * NO_CAR
    for i in range(m):
        tab_car[ord(motif[i])] = i
        decalage = 0
        res = []
        while(decalage <= n - m):
            j = m - 1
            while j >= 0 and motif[j] == txt[decalage + j]:
                j = j - 1
            if j < 0:
                res.append(decalage)
                if decalage + m < n :
                    decalage = decalage + m - tab_car[ord(txt[decalage + m])]
                else :
                    decalage = decalage + 1
            else:
                decalage = decalage + max(1, j - tab_car[ord(txt[decalage + j])])
    return res

def texte_alea(nombre):
    texte = ""
    alphabet = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s", "d", "f", "g", "h", "j", "k", "l", "m", "w", "x", "c", "v", "b", "n"]
    for _ in range(nombre):
        n = randint(0, 25)
        texte += alphabet[n]
    return texte
    