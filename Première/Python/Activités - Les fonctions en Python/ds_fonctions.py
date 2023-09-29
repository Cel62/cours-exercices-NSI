# Nom : Pihen
# Prénom : Céleste
# Classe : 1G5

import math

#### première fonction ####

# information : 1 miles est équivalent à 1,60934 kilométre
# la fonction round(a,b) permet d'arrondir un flottant a avec b chiffres après la virgule
# exemple round(5.65897, 2) renvoie 5.65

def convert_en_miles(valeur):
    """
    La fonction convert_en_miles prend comme argument une valeur en kilométres et renvoie la conversion en miles
    sous la forme d'un flottant arrondi à 2 chiffres après la virgule
    valeur : le nombre de kilomètres à convertir en miles
    type valeur : int
    return : la valeur convertie en miles
    rtype : float
    >>> convert_en_miles(100)
    62.14
    >>> convert_en_miles(12)
    7.46
    >>> convert_en_miles(235)
    146.02
    """
    miles = valeur / 1.60934
    return round(miles, 2)

#### première fonction ####

# Calcul de la distance en 3D : la distance euclidienne
# La distance à calculer est donnée par la relation distance_euclidienne = racine carré de ((xa-xb)^2 + (ya-yb)^2 + (za-zb)^2)

def distance_3D(xa,ya,za,xb,yb,zb):
    """
    La fonction distance_3D calcule (et tenvoie) la distance euclidienne en trois dimension entre deux points
    A(xa,ya,za) et B(xb,yb,zb) à partir de leurs coordonnées.
    xa, ya, za : les coordonnées du point A
    xb, yb, zb : les coordonnées du poiint B
    xa, ya, za, xb, yb, zb : int
    return : la distance euclidienne entre les points A et B
    rtype: float
    >>> distance_3D(0,0,0,1,1,1)
    1.73
    >>> distance_3D(1,1,1,1,5,1)
    4.0
    >>> distance_3D(0,0,0,5,4,2)
    6.71
    """
    from math import sqrt
    distance_euclidienne = sqrt((xa-xb)**2 + (ya-yb)**2 + (za-zb)**2)
    return round(distance_euclidienne, 2)
    

#### troisième fonction ####

# Qu'est qu'une année bissextile ?
# Une année bissextile est une année comportant 366 jours au lieu de 365 jours pour une année commune.
# Le jour supplémentaire, le 29 février, est placé après le dernier jour de ce mois qui compte habituellement 28 jours dans le calendrier grégorien
# L'année est est bissextile si :
#             elle est divisible par 4 et en même temps non divisible par 100
#             ou si l'année est divisible par 400 (« divisible » signifie que la division donne un nombre entier, sans reste).
# Sinon, l'année n'est pas bissextile : elle a la durée habituelle de 365 jours (elle est dite année commune).


def est_bissextile(annee):
    """
    La fonction est_bissextile prend comme argument un entier annee sous la forme AAAA
    et qui renvoie True si l'année est bissextile ou False dans le cas contraire
    type annee : int
    annee : année testée au format AAAA (exemple : 1982)
    rtype : booléen
    type : True si l'année est bissextile, False sinon
    >>> est_bissextile(1980)
    True
    >>> est_bissextile(2000)
    True
    >>> est_bissextile(1915)
    False
    >>> est_bissextile(1996)
    True
    """
    if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
        return True
    else:
        return False

import doctest
doctest.testmod(verbose = True)