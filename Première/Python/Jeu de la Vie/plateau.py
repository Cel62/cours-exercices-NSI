# Programme : plateau.py
# Nom : Pihen
# Prénom : Céleste
# version 1.0 créée le 09/02/23 en NSI

def creer_grille(nb_cases_horizontale, nb_cases_verticale):
    """
    Permet de créer une grille
    :type nb_cases_horizontale: int
    :type nb_cases_verticale: int
    :return: Renvoie une liste de listes correspondant à une grille de jeu aux dimensions souhaitées, ne contenant rien
    (ce qui correspondra à des cases remplies avec un zéro).
    :rtype: list
    :Example:
    >>> creer_grille(3,2)
    [[0, 0, 0], [0, 0, 0]]
    >>> creer_grille(3,3)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    """
    return [[0 for cases_horizontales in range(nb_cases_horizontale)] for cases_verticales in range(nb_cases_verticale)]

def hauteur_grille(grille):
    """
    Permet de connaître la hauteur de la grille
    :type grille: list
    :return: Renvoie le nombre de cases verticales
    :rtype: int
    :Example:
    >>> hauteur_grille(creer_grille(3,2))
    2
    """
    return len(grille)

def largeur_grille(grille):
    """
    Permet de connaître la largeur de la grille
    :type grille: list
    :return: Renvoie le nombre de cases horizontales
    :rtype: int
    :Example:
    >>> largeur_grille(creer_grille(3,2))
    3
    """
    return len(grille[0])

def creer_grille_aleatoire(dim_horizontale, dim_verticales, p):
    from random import random
    """
    Permet de créer une grille aléatoire
    :type dim_horizontale: int
    :type dim_verticales: int
    :type p: float
    :return: Renvoie une liste de listes correspondant à une grille de jeu aux dimensions souhaitées, avec une
    probabilité d'avoir une case occupée
    :rtype: list
    :Example:
    >>> creer_grille_aleatoire(3, 2, 1)
    [[1, 1, 1], [1, 1, 1]]
    >>> creer_grille_aleatoire(3, 2, 0)
    [[0, 0, 0], [0, 0, 0]]
    """
    grille = creer_grille(dim_horizontale, dim_verticales)
    for colonne in range(dim_horizontale):
        for ligne in range(dim_verticales):
            if random() <= p:
                grille[ligne][colonne] = 1
    return grille
    
def afficher_grille(grille):
    """
    Permet d'afficher la grille
    :type grille: list
    :return: Afficher de manière plus claire une grille de jeu
    :rtype: print
    :Example:
    >>> afficher_grille(creer_grille(3,2))
    ___
    ___
    """
    for ligne in range(hauteur_grille(grille)):
        for colonne in range(largeur_grille(grille)):
            if grille[ligne][colonne] == 1:
                print('O', end='')
            else:
                print('_', end='')
        print()

def voisins_case(grille, numero_ligne, numero_colonne):
    """
    Permet de voir les cases voisines
    :type grille: list
    :type numero_ligne: int
    :type numero_colonne: int
    :return: Le nombre de valeurs retournées dans la liste correspond au nombre de voisines de la case
    :rtype: list
    :Example:
    >>> voisins_case([[0, 1, 0], [1, 0, 0], [1, 1, 1]], 1, 1)
    [0, 1, 0, 1, 0, 1, 1, 1]
    >>> voisins_case([[0, 1, 0], [1, 0, 0], [1, 1, 1]], 2, 2)
    [0, 0, 1]
    >>> voisins_case([[0, 1, 0], [1, 0, 0], [1, 1, 1]], 0, 2)
    [1, 0, 0]
    """
    liste = []
    for ligne in range(numero_ligne - 1, numero_ligne + 2):
        for colonne in range(numero_colonne - 1, numero_colonne + 2):
            if (ligne, colonne) != (numero_ligne, numero_colonne) and ligne >=0 and colonne >=0 and ligne < hauteur_grille(grille) and colonne < largeur_grille(grille):
                liste.append(grille[ligne][colonne])
    return liste
    
def nb_cases_voisins_occup(grille, numero_ligne, numero_colonne):
    """
    Permet d'obtenir le nombre de cases occupées dans le voisinage
    :type grille: list
    :type numero_ligne: int
    :type numero_colonne: int
    :return: Renvoie le nombre de cases occupées dans les cases voisines de la case passée en paramètre
    :rtype: int
    :Example:
    >>> nb_cases_voisins_occup([[0, 1, 0], [1, 0, 0], [1, 1, 1]], 1, 1)
    5
    >>> nb_cases_voisins_occup([[0, 1, 0], [1, 0, 0], [1, 1, 1]], 2, 2)
    1
    """
    return sum(voisins_case(grille, numero_ligne, numero_colonne))

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)