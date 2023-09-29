# Le jeu de la vie

### Présentation

Le jeu de la vie est un automate cellulaire : ensemble de cellules représenté par une grille qui peut évoluer au cours du temps. En réponse à un problème de John von Neumann qui recherchait une machine capable d'auto-réplication, John Horton Conway, en 1970, a construit ce modèle mathématique basé sur un algorithme avec des règles basiques.
Aujourd'hui, les automates cellulaires, comme le jeu de la vie, sont utilisés dans des simulations informatiques : évolution des cellules vivantes dans un organisme, évolution de certaines populations...

Le jeu de la vie est une modélisation simpliste de la vie de cellules dans l'espace. Dans le cadre de cet exercice l'espace sera une grille rectangulaire dont chaque case peut contenir au plus une cellule. Chaque case contiendra donc soit 0 soit 1 cellule. 

Les cellules peuvent émerger ou mourir selon des critères précis à réévaluer à chaque nouvelle génération :

1. Une cellule émergera dans une case qui possède exactement trois voisines
   avec une cellule.
2. Une cellule disparaît de sa case si elle est entourée par strictement moins
   de deux cellules vivantes ou strictement plus de trois cellules vivantes.
3. Les autres cases restent dans leur état.

Les voisines prises en compte sont toutes les cases situées immédiatement à
gauche, à droite, en haut, en bas ou sur les quatre diagonales, si elles existent.
Une case a donc au plus 8 voisines, moins si elle se situe sur un bord de la grille.

Voir la [vidéo didactique](https://www.youtube.com/watch?v=S-W0NX97DB0) de David Louapre présente le jeu de la vie (et des structures complexes).

### Génération suivante

Commencer par ouvrir le fichier `jeu_de_la_vie.py`, dans lequel on importe le fichier `plateau.py` (le votre ou celui fourni comme correction) afin d'utiliser les fonctions déjà réalisées.

Nous allons maintenant réaliser une fonction `generation_suivante` qui, à partir d'une grille passée en paramètre, calcule la grille de la génération suivante et la retourne. 

La nouvelle génération est calculée à partir des critères d'émergence ou de mort
des cellules indiqués au début de l'énoncé.

Dans le jeu de la vie, on considère que la nouvelle génération apparaît spontanément dans toutes les cellules au même moment.

Pour cela, commencer par créer une `grille_temp` qui sera une grille temporaire de mêmes dimensions que la grille passée en paramètre mais remplie de zéro. C'est cette grille que vous modifirez en parcourant la grille passée en paramètre et en y appliquant les régles du jeu de la vie.

```python
grille = [[0, 1, 0], [1, 0, 0], [1, 1, 1]]
>>> generation_suivante(grille)
[[0, 0, 0], [1, 0, 1], [1, 1, 0]]
>>> generation_suivante([[0, 0, 0], [1, 0, 1], [1, 1, 0]])
[[0, 0, 0], [1, 0, 0], [1, 1, 0]]
>>> generation_suivante([[0, 0, 0], [1, 0, 0], [1, 1, 0]])
[[0, 0, 0], [1, 1, 0], [1, 1, 0]]
```

### Évolution au fil de n générations

Nous allons réaliser une procédure `evolution_n_generations` qui prend en paramètre une grille et un entier naturel `n` et qui va afficher l'évolution de la grille au fil de `n` générations. 

**Remarque :** on parle de procédure et pas de fonction car on ne retourne rien , on se contente de modifier la grille et de l'afficher.

Afin de mieux visualiser l'évolution nous ferons une pause d'une seconde entre chaque génération. La fonction `sleep` du module `time` vous permettra de faire une telle pause (allez voir la documentation de cette fonction pour savoir comment l'utiliser).

### Motifs récurrents

Quelques motifs récurrents peuvent être obtenus à partir de grilles particulières.

Par exemple, un oscillateur à deux états peut être obtenu avec cette grille :

```python
grille = [[0, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0]]
```

Le planeur est un motif qui se déplace jusqu'à disparaître de la grille. Voici une grille permettant d'obtenir un planeur qui se répète toutes les quatre générations en s'étant déplacé d'une case vers le bas et d'une case vers la droite à chaque génération :

```python
grille = [[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
```

Vous trouverez des motifs plus complexes sur la [page Wikipedia du jeu de la
vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie#Structures), en particulier dans sa [version anglophone](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life#Examples_of_patterns).

Mais aussi sur [http://www.cypris.fr/loisirs/le_jeu_de_la_vie/jeu_de_la_vie.htm](http://www.cypris.fr/loisirs/le_jeu_de_la_vie/jeu_de_la_vie.htm)

### Interface graphique

Dans le même répertoire que les fichiers `plateau.py` et `jeu_de_la_vie.py` , ajouter le programme `jeu_de_la_vie_tkinter.py` fourni.

Lancez ce dernier et observez !!!

### Plus de vidéos

A grande échelle :

[https://www.youtube.com/watch?v=so7XunsVDOo](https://www.youtube.com/watch?v=so7XunsVDOo)

[https://www.youtube.com/watch?v=-FaqC4h5Ftg](https://www.youtube.com/watch?v=-FaqC4h5Ftg)

[https://www.youtube.com/watch?v=Su1Uu4_wIak](https://www.youtube.com/watch?v=Su1Uu4_wIak)

En 3D :

https://www.youtube.com/watch?v=_W-n510Pca0


