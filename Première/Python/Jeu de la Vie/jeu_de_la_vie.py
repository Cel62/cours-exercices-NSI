from plateau import *
from time import sleep
    
def generation_suivante(grille):
    '''
    Permet d'obtenir la génération suivante
    :type grille: list
    :return: Renvoie la génération suivante
    :rtype: list
    :Examplec:
    >>> generation_suivante([[0, 1, 0], [1, 0, 0], [1, 1, 1]])
    [[0, 0, 0], [1, 0, 1], [1, 1, 0]]
    >>> generation_suivante([[0, 0, 0], [1, 0, 1], [1, 1, 0]])
    [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
    >>> generation_suivante([[0, 0, 0], [1, 0, 0], [1, 1, 0]])
    [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    '''
    
    grille_temp = creer_grille(hauteur_grille(grille), largeur_grille(grille))
    
    for ligne in range(hauteur_grille(grille)):
        for colonne in range(largeur_grille(grille)):
            nb_cellules_voisines = nb_cases_voisins_occup(grille, ligne, colonne)
            
            if nb_cellules_voisines == 3:
                grille_temp[ligne][colonne] = 1
                
            elif nb_cellules_voisines < 2 or nb_cellules_voisines > 3:
                grille_temp[ligne][colonne] = 0
                
    return grille_temp
    
def evolution_n_generations(grille, n):
    '''
    
    '''
    pass
    # mise en place d'une boucle avec n répétitions
    
    # pause d'une seconde avec sleep(1)
    
    # creation d'une nouvelle grille à partir de generation_suivante(grille)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)