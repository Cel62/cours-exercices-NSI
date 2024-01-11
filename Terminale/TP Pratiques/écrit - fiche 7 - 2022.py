def chiffrer(mot, alpha):
    mot_final = ""
    for lettre in mot:
        mot_final += alpha[lettre]
    return mot_final

def dico_dechiffrement(dico):
    dico_dechiff = {}
    for cle in dico:
        dico_dechiff[dico[cle]] = cle
    return dico_dechiff

def dechiffre(mot, dico):
    return chiffrer(mot, dico_dechiffrement(dico))

def dico_chiffrement(alphabet):
    from random import shuffle
    
    dico = {}
    
    alphabet2 = alphabet.copy()
    
    shuffle(alphabet)

    for i in range(len(alphabet)):
        dico[alphabet[i]] = alphabet2[i]

    return dico