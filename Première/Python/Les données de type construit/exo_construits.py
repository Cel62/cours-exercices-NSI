#chaine = 'Je découvre les chaines de caractères avec Python'
#print(len(chaine))
#print(type(chaine))
#print(chaine[11])
#print(chaine[26:37])

def est_presente(chaine, lettre):
    return lettre in chaine

def rang_lettre(chaine, lettre):
    posLetter = []
    for index in range(len(chaine)):
        if lettre == chaine[index]:
            posLetter.append(index)
    return posLetter

# semaine = ['lundi', 'tuesday', 'mercredi', 'jeudi', 'vendredi', 'samedi']
# semaine.append('dimanche')
# print(semaine)
# print(semaine[2])
# semaine[1] = 'mardi'
# print(semaine)
# for index in range(len(semaine)):
#     print('item', index + 1, ':', semaine[index])
# for jour in semaine:
#     print (jour)
    
def select(numero):
    mois = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    if numero <= 0 or numero > 12:
        return "Vous devez choisir un nombre entre 1 et 12."
    else:
        return mois[numero - 1]

# carre = []
# for i in range(11):
#     carre.append(i**2)
# 
# carre_comprehension = [i**2 for i in range(11)]

def mot_plus_long(chaine):
    mots = chaine.split()
    motlong = ""
    for mot in mots:
        if len(mot) > len(motlong):
            motlong = mot
    return motlong 

# valeurs_x = [i+1 for i in range(-11, 10)]
# valeurs_y = [x**2 - 2*x + 3 for x in valeurs_x]
# import matplotlib.pyplot as plt
# plt.plot(valeurs_x, valeurs_y)
# plt.show()

def produit(nombres, n):
    resultat = [nombre*n for nombre in nombres]
    return resultat

# def pair_impair(uplet):
#     nb_pairs = ()
#     nb_impairs = ()
#     for nombre in uplet:
#         if nombre % 2 == 0:
#             nb_pairs = nombre
#         else:
#             nb_impairs = nombre
#     return nb_pairs and nb_impairs

