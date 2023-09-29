aliens = [['jaune','moyenne','léger','non','non'],
         ['jaune','grande','moyen','oui','oui'],
         ['vert','petite','moyen','oui','oui'],
         ['jaune','petite','moyen','non','non'],
         ['rouge','moyenne','lourd','non','non'],
         ['vert','grande','lourd','non','oui'],
         ['vert','moyenne','lourd','non','oui'],
         ['jaune','petite','léger','oui','oui']]

nouvel_alien1 = ['jaune','grande','moyen','oui']

def distance_couleur(x, y):
    if x[0] == y[0]:
        return 0
    else:
        return 1

def distance_taille(x, y):
    if x[1] == y[1]:
        return 0
    elif (x[1] == "petite" and y[1] == "grande") or (x[1] == "grande" and y[1] == "petite"):
        return 1
    else:
        return 0.5
    
def distance_poids(x, y):
    if x[2] == y[2]:
        return 0
    elif (x[2] == "léger" and y[2] == "lourd") or (x[2] == "lourd" and y[2] == "léger"):
        return 1
    else:
        return 0.5
    
def distance_ypp(x, y):
    if x[3] == y[3]:
        return 0
    else:
        return 1

def distance_globale(x, y):
    from math import sqrt
    return sqrt(distance_couleur(x, y)**2 + distance_taille(x,y)**2 + distance_poids(x, y)**2 + distance_ypp(x, y)**2)

def liste_ordonnee_voisins(x):
    liste = []
    for i in range(len(aliens)):
        liste.append((distance_globale(x, aliens[i]), i))
        liste.sort()
    return liste

def bellicosite(x, k):
    l = liste_ordonnee_voisins(x)
    r = 0
    for i in range(k):
        if l[0][0] == 0.0:
            if aliens[l[j][1][4]] == "oui":
                return "alien déjà existant, belliqueux"
            else:
                return "alien déjà existant, non belliqueux"
        if aliens[l[j][1][4]] == "oui":
            r = r + 1
        else:
            r = r - 1
    if r >= 0:
        x.append("oui")
        f = open("star wars bellicosité.txt", "a")
        f.write(str(x) + "\n")
        f.close()
        aliens.append(x)
        return aliens
    else:
        x.append("non")
        f = open("star wars bellicosité.txt", "a")
        f.write(str(x) + "\n")
        f.close()
        aliens.append(x)
        return aliens

def fichier():
    f = open("star wars bellicosité.txt", "a")
    f.write(''.join(str(e) + "\n" for e in aliens))
    f.close()