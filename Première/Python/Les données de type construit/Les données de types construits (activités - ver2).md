# Les données de type construit (activités)

Ces exercices seront à rendre sous la forme d'un unique fichier nommé `exo_construits.py`

### Exercice 1

Dans un programme, créer une variable `chaine` contenant la phrase "Je découvre les chaines de caractères avec Python" et qui affichera une phrase (ou plusieurs) qui donnera :

* la longueur de la chaîne de caractères

* le type de la variable `chaine` 

* le 12ème caractère de la chaîne

* la portion de la chaîne du 27ème au 37ème caractères

### Exercice 2

Créez une fonction `est_presente` qui prend en paramètre une chaîne de caractère nommée `chaine` et une lettre nommée `lettre` et qui retourne un booléen si la `lettre`  demandée est présente dans la `chaine`.

### Exercice 3

Créez une fonction `rang_lettre` qui prend en paramètre une chaîne de caractère nommée `chaine` et une lettre nommée `lettre` et qui retourne une liste indiquant les indices où se trouve la lettre recherchée dans la chaine.

```python
# exemples
>>>rang_lettre('une apparition','a')
[4, 7]
>>>rang_lettre('une apparition','i')
[9, 11]
```

### Exercice 4

Soit la liste ci-dessous :

```python
semaine = ['lundi', 'tuesday', 'mercredi', 'jeudi', 'vendredi', 'samedi']
```

Ajouter les instructions nécessaires :

* pour ajouter la journée de 'dimanche' à la liste

* pour afficher l'item 'mercredi'

* pour remplacer l'item 'tuesday' par 'mardi'

* pour afficher comme ci-dessous tous les items de la liste en utilisant une boucle `for` et en parcourant tous les indices.
  
  ```python
  item 1 : lundi
  item 2 : mardi
  ...
  ```

* pour afficher comme ci-dessous tous les items de la liste en utilisant une boucle `for` et `in` .
  
  ```python
  lundi
  mardi
  ...
  ```

### Exercice 5

Écrire une fonction `select` qui prend en paramètre le numéro d'un mois (de 1 à 12) et qui retourne le mois sélectionné.

Remarque : il faut créer une liste appelée `mois` qui contiendra tous les mois de l'année.

```python
mois = [janvier, février, ....]
```

### Exercice 6

Créer une liste nommé `carre` contenant le carré des nombres entiers n allant de 0 à 10 en utilisant une boucle for.

Créer ensuite une liste nommée `carre_comprehension`  identique à la précédente mais en utilisant par la méthode par compréhension de liste.

### Exercice 7

Créez une fonction `mot_plus_long` qui prend en paramètre une chaîne de caractère nommée `chaine` et qui retourne le premier mot le plus long contenu dans la chaine.

```python
# exemples
>>>mot_plus_long('voici une suite de mots pour faire une phrase')
phrase
```

**Remarque :** il faut utiliser la méthode `split()` sur la chaine de caractère pour construire une liste de mots.

### Exercice 8

On considère la fonction mathématique $y = x^{2} - 2x +3$ .

Ecrire un programme qui stocke dans deux listes : 

* les valeurs entières de x allant de -10 à 10 dans `valeurs_x`

* les valeurs associées de y dans `valeurs_y` pour x allant de -10 à 10

<u>Pour les plus avancés</u>, ajouter ensuite à votre programme les lignes de code ci-dessous et observer.

```python
# le code à ajouter
import matplotlib.pyplot as plt
plt.plot(valeurs_x, valeurs_y)
plt.show()
```

### Exercice 9

Créez une fonction `produit` qui prend en paramètre une liste de nombre nommée `nombres` et un entier naturel non nul nommé `n` et qui renvoie une nouvelle liste obtenue en multipliant chaque élément de la liste `nombres` par `n`.

Pour les plus avancés, proposer une fonction `produit2` identique à la fonction `produit` mais utilisant la méthode par compréhension de liste.

```python
# exemplehg
>>> produit([1, 2, 4, 5], 2)
[2, 4, 8, 10]
```

### Exercice 10

Créez une fonction `pair_impair` qui prend en paramètre un tuple nommé `uplet` composé d'entiers et qui renvoie un tuple composé de deux listes : une première qui contient les nombres pairs et une deuxième qui contient les nombres impairs.

<u>Pour les plus avancés</u>, faire le nécessaire pour que les listes renvoyées dans le tuple soient triées dans l'ordre croissant.

<u>Pour les encore plus avancés</u>, créer une fonction `pair_impair2` jouant le même rôle que la fonction précédente mais en utilisant la méthode par compréhension (pas utile de trier par ordre croissant les résultats).

```python
# exemple
>>> pair_impair((1, 5, 2, 8, 7))
[2, 8],[1, 5, 7]
```

### Exercice 11

Créez une fonction `table`qui prend un paramètre `n` et qui retourne un tableau de taile n x n, tel que `table_multiplication[i][j]` (qui est un tableau construit avec la fonction `table`) contient le produit de i fois j.

<u>Pour les plus avancés</u>, faire une fonction `affichage` qui permet d'afficher le tableau généré par la fonction `table` comme ci-dessous :

```python
>>> affichage(table(5))
0    0    0    0    0    
0    1    2    3    4    
0    2    4    6    8    
0    3    6    9    12    
0    4    8    12    16
```

### Exercice 12

Créez une fonction `aleatoire` qui ne prend pas de paramètre et qui retourne un tableau à deux dimensions de taille 10 x 10 contenant des nombres entiers tirés au hasard entre 0 et 10.

```python
>>> aleatoire()
[[5, 7, 9, 9, 2, 10, 3, 2, 4, 0], [6, 0, 5, 3, 10, 7, 5, 6, 5, 8], [3, 7, 9, 10, 6, 7, 0, 2, 4, 8], [9, 7, 5, 9, 0, 0, 3, 6, 1, 1], [5, 3, 4, 6, 2, 10, 2, 0, 6, 8], [9, 4, 0, 10, 7, 2, 2, 9, 2, 10], [0, 9, 9, 10, 4, 2, 5, 4, 1, 9], [9, 6, 9, 5, 7, 5, 7, 5, 9, 9], [2, 5, 7, 9, 3, 2, 6, 0, 5, 0], [10, 9, 0, 5, 2, 4, 9, 6, 8, 3]]
```

Pour les plus avancés, créer une fonction nommée `comptage` qui retourne une liste donnant le nombre de 1, de 2, de 3.... contenu dans le tableau obtenu avec la fonction `aleatoire`.

```python
>>> comptage(aleatoire())
[11, 3, 12, 7, 7, 13, 9, 9, 4, 17, 8]
```

### Exercice 13

Le Scrabble est un jeu de société où l'on doit former des mots avec un tirage aléatoire de lettres, chaque lettre valant un certain nombre de points.

Vous trouverez dans la [règle du jeu](https://www.regles-de-jeux.com/regle-du-scrabble/) la valeur de chaque point.

Construire un dictionnaire nommé `scrabble` avec comme `clés` les lettres de l'alphabet et comme `valeurs` le nombre de point associé.

**Attention :** Les lettres du scrabble sont exclusivement en majuscule !

Créer ensuite une fonction nommée `score` qui prend en argument un `mot` et qui retourne le total des points pour le mot choisi.

**Remarque :** on ne tiendra pas compte des lettres jokers et des cases "mot compte double ou triple" du plateau.

<u>Pour les plus avancés :</u> ajouter au dictionnaire précédent le nombre de chacune des lettres en plus de sa valeur (sous forme d'une liste pour chaque lettre) et créer une fonction `tirage_au_sort` qui renvoie une liste de sept lettres en tenant compte des lettres déjà tirées.

**Remarque :** il faudra modifier la fonction `score` pour tenir compte de la changement de la structure du dictionnaire `scrabble`.

*Aide :* pour tirer au sort un clé d'un dictionnaire :

```python
import random
lettre = choice(list(scrabble.keys()))
```
