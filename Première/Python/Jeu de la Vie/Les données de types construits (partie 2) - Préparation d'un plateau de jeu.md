# Les données de types construits (partie 2)

### Consignes et objectifs

Cette série d'exercices est à rendre sous la forme d'un unique fichier `plateau.py`

L'idée de cette série d'exercices est de manipuler des données de types construits afin de construite un plateau de jeu.

### Introduction

Beaucoup de jeux (les échecs, les dames, le puissance 4, ...) ou de simulation se déroulent sur un plateau (ou grille).

Du point de vue technique une grille du jeu peut être représentée par une
liste de listes de nombre entiers. Chaque nombre entier représente l'occupation d'une case : 

* 0 si elle est vide

* 1 si elle est occupée

```python
# exemple de grille
[[0, 1, 0],[1, 0, 0]]
```

La liste ci-dessus représente une grille de jeu de 6 cases, 3 cases en largeur et 2 cases en hauteur. Sur la première ligne seule la deuxième case possède une cellule, tandis que sur la deuxième ligne, seule la première case en possède une.

**Remarque :** la représentation mise en place ci-dessus est suffisante pour un jeu simple où seule l'occupation de la case est utile. Si on veut représenter un jeu de dame, il faudrait mettre en place un autre codage, par exemple :

* La lettre B pour un pion blanc

* La lettre N pour un pion noir

Et il faudrait en plus réfléchir au codage des dames blanches et noires...

Et si on imaginait la représentation d'un plateau d'échec ?

Ou une bataille navale ?

### Exercice 1 : Construction d'une grille vide

Réalisez une fonction `creer_grille` qui prend en paramètre le nombre de cases
horizontalement, puis verticalement et qui renvoie une liste de listes correspondant à une grille de jeu aux dimensions souhaitées, ne contenant rien (ce qui correspondra à des cases remplies avec un zéro).

```python
>>> creer_grille(3, 2)
[[0, 0, 0], [0, 0, 0]]
```

### Exercice 2 : Dimensions d'une grille

Réalisez une fonction `hauteur_grille` qui prend en paramètre une grille de
jeu et qui renvoie le nombre de cases verticales.

```python
>>> hauteur_grille(creer_grille(3, 2))
2
```

Réalisez une fonction `largeur_grille` qui prend en paramètre une grille de
jeu et qui renvoie le nombre de cases horizontales.

```python
>>> largeur_grille(creer_grille(3, 2))
3
```

### Exercice 3 : Initialisation d'une grille

La grille créée par la fonction `creer_grille` ne contient rien (il n'y a que des zéros). 

Réalisez une fonction `creer_grille_aleatoire` qui prend en paramètre les
dimensions horizontales et verticales de la grille et une probabilité *p* (qui correspond à  la probabilité pour une case de la grille d'être occupée).

La probabilité est un nombre compris entre 0 et 1, si p = 0,35 cela veut dire qu'il y a 35% de chance que la case soit occupée.

Il faudra importer la méthode `random()` de la bibliothèque `random` !

```python
>>> creer_grille_aleatoire(3, 2, 1)
[[1, 1, 1], [1, 1, 1]]
>>> creer_grille_aleatoire(3, 2, 0)
[[0, 0, 0], [0, 0, 0]]
>>> creer_grille_aleatoire(3, 2, 0.5)
[[1, 0, 1], [0, 0, 1]]
```

**Remarque :** La méthode random() de la bibliothèque random génére un nombre pseudo-aléatoire compris entre 0 et 1. Si on veut faire un tirage au sort avec une propabilité p, on pourra s'inspirer de l'exemple ci-dessous.

```python
# Générer une probabilité p avec 32 % de chance de gagner à ce jeu...
if random() <= 0.32:
    print("gagné")
else:
    print("perdu")
```

### Exercice 4 : Afficher une grille

Visualiser une grille sous forme de listes de listes n'est pas aisé. Nous allons donc réaliser une procédure `afficher_grille` dont le rôle sera d'afficher de manière plus claire une grille de jeu qui lui est passée en paramètre. Les cases vides seront affichées avec un tiret bas (`_`) et les cases contenant quelque chose seront affichées avec un O majuscule (`O`). 

Le contenu des cases sera séparé par une espace. 

Chaque ligne de la grille sera affichée sur une ligne distincte.

C'est la **seule** fonction (ou procédure) qui pourra utiliser un `print`.

Pour les exemples qui suivent (jusqu'à la fin de l'énoncé), nous considérons définie une variable `grille` qui permettra de faire vos essais :

```python
grille = [[0, 1, 0], [1, 0, 0], [1, 1, 1]]
```

```python
>>> afficher_grille(grille)
_ O _
O _ _
O O O
>>> afficher_grille(creer_grille(3, 2))
_ _ _
_ _ _
```

### Exercice 5 : Voisins d'une case

Réalisez une fonction `voisins_case` qui prend en paramètre une grille de jeu ainsi que les coordonnées en abscisse et en ordonnée d'une case (la coordonnée 0,0 étant la case en haut à gauche). La fonction renvoie une liste contenant la valeur des cases voisines de la case donnée en paramètre.
Le nombre de valeurs retournées dans la liste correspond au nombre de voisines de la case (au plus huit, moins quand elle se trouve sur un bord de la grille).
L'ordre dans lequel les valeurs sont renvoyées n'est pas spécifié. Cependant dans l'exemple ci-dessous les valeurs des cases voisines sont renvoyées ligne par ligne, de gauche à droite.

```python
>>> voisins_case(grille, 1, 1)
[0, 1, 0, 1, 0, 1, 1, 1]
>>> voisins_case(grille, 2, 2)
[0, 0, 1]
>>> voisins_case(grille, 0, 2)
[1, 0, 0]
```

### Exercice 6 : nombre de cases occupées dans le voisinage

Réalisez une fonction `nb_cases_voisins_occup` qui prend en paramètre une grille
ainsi que les coordonnées d'une case et qui renvoie le nombre de cases occupées dans
les cases voisines de la case passée en paramètre.

```python
>>> nb_cases_voisins_occup(grille, 1, 1)
5
>>> nb_cases_voisins_occup(grille, 2, 2)
1
```
