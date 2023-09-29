### Mini-projet : Gestion des vLille

Récupérer sur le site [https://opendata.lillemetropole.fr/explore/dataset/vlille-realtime/information/](https://opendata.lillemetropole.fr/explore/dataset/vlille-realtime/information/) le fichier `vlille-realtime.csv` donnant en temps réel la disponibilité des vélos V'Lille de la métropole Lilloise et le placer dans le dossier contenant votre programme.

Réalisez une fonction `lecture` qui prend en paramètre le nom du fichier csv obtenu précedemment et qui retourne une liste de dictionnaires avec comme descripteurs les noms des entêtes du fichier csv.

**<u>Attention :</u>** le caractère séparateur de ce fichier csv est le point virgule de plus l'encodage des caractère est utf-8, apportez les corrections nécessaires en étudiant la documentation du module csv disponible en suivant ce lien : [https://docs.python.org/fr/3/library/csv.html](https://docs.python.org/fr/3/library/csv.html)

Faire ensuite les activités suivantes :

- Réalisez une fonction `velo_endroit` qui ne prend pas de paramètre, et qui renvoie la liste des noms des endroits où se trouvent une zone de dépôt de vélos.

- Réalisez une fonction `velo_dispo` qui ne prend pas de paramètre, et qui renvoie la liste des noms des endroits où se trouvent des vélos disponible.

- Réalisez une fonction `velo_non_dispo` qui ne prend pas de paramètre, et qui renvoie la liste des noms des endroits où il n'y plus de vélo disponible.

- Réalisez une fonction `station_hs` qui ne prend pas de paramètre et qui renvoie la liste des noms des endroits la station est hors service.

- Réalisez une fonction `info_depot` qui prend en paramètre le numéro du dépôt sous la forme d'un identifiant et qui retourne : le nom du dépôt, son adresse (adresse + commune), et le nombre de vélo disponible sous forme d'un tuple.

- Réalisez une fonction `recherche_station` qui prend en paramètre une chaine de caractère (en lettres majuscules), et qui renvoie une liste des dépôts (des tuples avec nom et identifiant) contenant cette chaîne.

- Réalisez une fonction `recherche_station_carte` qui prend en paramètre une chaine de caractère (en lettres majuscules) et qui recherche les noms de dépôt contenant cette chaîne et les placent sur une carte avec des marqueurs indiquant le nom de la station et son identifiant (utiliser folium).

Pour les plus avancés : réalisez une fonction `dispo_proche` qui prend en paramètres l'identifiant d'un dépôt et une distance en mètre, et qui affiche la liste des dépôts situés à moins de cette distance (à vol d'oiseau) sous forme de marqueurs sur une carte (mettre une couleur différente si le dépôt est vide). On utilisera la méthode `distance` du module `geopy` dont la documentation se trouve à l'adresse [https://geopy.readthedocs.io/en/stable/](https://geopy.readthedocs.io/en/stable/) pour calculer les distances à partir de coordonnées GPS.
