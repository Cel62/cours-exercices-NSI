# Activités - Traitement des données en table

### Exercice n°1

* Téléchargez le fichier `identite.csv`, et placez-le dans le même dossier que votre programme Python.

* Ecrire une fonction `lecture` qui prend en paramètre le nom du fichier à ouvrir, et qui retourne le contenu du fichier csv sous forme d'une liste de dictionnaires ayant pour clés les entêtes de la première ligne (fonction déjà créée dans le fichier réponse `exos_vide.py`)
  
  ```python
  >>> lecture('identite.csv')
  [{'nom': 'Durand', 'prenom': 'Jean-Pierre', 'date_naissance': '23/05/1985'}, {'nom': 'Dupont', 'prenom': 'Christophe', 'date_naissance': '15/12/1967'}, {'nom': 'Terta', 'prenom': 'Henry', 'date_naissance': '12/06/1978'}, {'nom': 'Turing', 'prenom': 'Alan', 'date_naissance': '23/06/1912'}, {'nom': 'Lovelace', 'prenom': 'Ada', 'date_naissance': '10/12/1815'}]
  ```

* Afin d'utiliser facilement les données issues du fichier csv : `ìdentite.csv`, mofifiez la ligne n°9 de votre programme avec :
  
  ```python
  donnees = lecture('identite.csv')
  ```

* Ecrire une fonction `is_present` qui prendra en paramètre un prénom et qui renvoie True si le prénom est dans les données et False sinon.
  
  ```python
  >>> is_present('Henry')
  True
  >>> is_present('Marcel')
  False
  ```

* Ecrire une fonction `date_naissance()` qui prendra en paramètre un nom et qui renvoie la date de naissance correspondante si le nom fait partie de la liste.
  
  ```python
  >>> date_naissance('Lovelace')
  '10/12/1815'
  ```

### Exercice n°2

Afin d'avoir des exemples plus complexes à traiter, dans la suite, nous allons travailler sur les données contenues dans le fichier `villes.csv` ce fichier contient des informations sur plus de 36000 villes françaises.

* Ouvrir le fichier avec notepad++ afin de découvrir les informations contenues dans ce fichier.

* Tester la fonction `lecture`  avec le fichier `villes.csv` et vérifier qu'elle retourne le contenu du fichier csv sous forme d'une liste de dictionnaires ayant pour clés les entêtes de la première ligne. Vous devriez alors obtenir ceci (en beaucoup plus grand) :
  
  ```python
  >>> lecture('villes.csv')
  [{'dep': '1', 'nom': 'Ozan', 'cp': '1190', 'nb_hab_2010': '618', 'nb_hab_1999': '469', 'nb_hab_2012': '500', 'dens': '93', 'surf': '6.6', 'long': '4.91667', 'lat': '46.3833', 'alt_min': '170', 'alt_max': '205'}, {'dep': '1', 'nom': 'Cormoranche-sur-SaÃ´ne', 'cp': '1290', 'nb_hab_2010': '1058', 'nb_hab_1999': '903', 'nb_hab_2012': '1000', 'dens': '107', 'surf': '9.85', 'long': '4.83333', 'lat': '46.2333', 'alt_min': '168', 'alt_max': '211'}...]
  ```

* Vous constatez que la ville de 'Cormoranche-sur-Saône' (et d'autres) ne s'affiche pas correctement à cause d'un encodage de caractères mal configuré. Le fichier csv ayant été encodé en `UTF-8`, proposez une correction de votre fonction `lecture` afin de tenir compte de cet encodage.
  
  <u>Aide :</u> documentation module csv ([https://docs.python.org/fr/3/library/csv.html](https://docs.python.org/fr/3/library/csv.html))
  
  Vous obtenez maintenant (pour le début) :
  
  ```python
  >>> lecture('villes.csv')
  [{'dep': '1', 'nom': 'Ozan', 'cp': '1190', 'nb_hab_2010': '618', 'nb_hab_1999': '469', 'nb_hab_2012': '500', 'dens': '93', 'surf': '6.6', 'long': '4.91667', 'lat': '46.3833', 'alt_min': '170', 'alt_max': '205'}, {'dep': '1', 'nom': 'Cormoranche-sur-Saône', 'cp': '1290', 'nb_hab_2010': '1058', 'nb_hab_1999': '903', 'nb_hab_2012': '1000', 'dens': '107', 'surf': '9.85', 'long': '4.83333', 'lat': '46.2333', 'alt_min': '168', 'alt_max': '211'},...]
  ```

* Ecrire une fonction `liste_villes` qui prend en paramètres : le nom du fichier csv et qui retourne la liste de toutes les villes contenues dans le fichier.
  
  ```python
  >>> liste_villes('villes.csv')
  ['Ozan', 'Cormoranche-sur-Saône', 'Plagne', 'Tossiat', 'Pouillat', 'Torcieu', 'Replonges', 'Corcelles', 'Péron', 'Relevant', 'Chaveyriat', 'Vaux-en-Bugey', 'Maillat', 'Faramans', 'Béon', 'Saint-Bernard',...]
  ```

* Ecrire une fonction `liste_villes_altitude_min` qui prend en paramètres : le nom du fichier csv et une altitude et qui renvoie la liste des villes ayant une altitude  minimum plus grande que la valeur donnée en paramètre (par exemple la liste des villes d'altitude minimum supérieure ou égale à 1500 m).
  
  ```python
  >>> liste_villes_altitude_min('villes.csv', 1500)
  ['Larche', 'Ristolas', 'Saint-Véran', 'Molines-en-Queyras', 'Abriès', "Villar-d'Arêne", 'La Llagonne', 'Caudiès-de-Conflent', 'Porté-Puymorens', 'Mont-Louis', 'Angles', 'Bessans', "Val-d'Isère", 'Bonneval-sur-Arc']
  ```

* Ecrire une fonction `liste_villes_altitude_max` qui prend en paramètres : le nom du fichier csv et une altitude et qui renvoie la liste des villes ayant une altitude maximum plus grande que la valeur donnée en paramètre (par exemple la liste des villes d'altitude maximum supérieure ou égale à 4000 m).
  
  ```python
  >>> liste_villes_altitude_max('villes.csv', 4000)
  ['Pelvoux', 'Saint-Christophe-en-Oisans', 'Chamonix-Mont-Blanc', 'Houches', 'Saint-Gervais-les-Bains']
  ```
  
  Comparez votre résultat avec une recherche sur internet des 5 villes les plus hautes de France !

* Ecrire une fonction `densite_max` qui prend en paramètres : le nom du fichier csv et une valeur de densité et qui renvoie la liste des villes ayant une densité d'habitant inférieure ou égale à la valeur passée en paramètre.
  
  ```python
  >>> densite('villes.csv', 50)
  ['Plagne', 'Pouillat', 'Corcelles', 'Relevant', 'Béon', 'Rossillon', 'Chavannes-sur-Reyssouze', 'Flaxieu', 'Hotonnes', 'Songieu', 'Virieu-le-Petit', 'Marchamp', 'Mantenay-Montlin',...]
  ```

* Ecrire une fonction `altitude_densite` qui prend en paramètres : le nom du fichier csv, une altitude et une valeur de densité et qui renvoie la liste des villes ayant une densité d'habitant inférieure ou égale **<u>et</u>** une altitude minimum supérieure aux valeurs passées en paramètres.
  
  Remarque : Utilisez vos fonctions déjà créées !
  
  ```python
  >>> altitude_densite('fichier.csv', 1500, 50)
  ['Larche', 'Ristolas', 'Saint-Véran', 'Molines-en-Queyras', 'Abriès', "Villar-d'Arêne", 'La Llagonne', 'Caudiès-de-Conflent', 'Porté-Puymorens', 'Angles', 'Bessans', "Val-d'Isère", 'Bonneval-sur-Arc']
  ```

* Ecrire une fonction `altitude_min_moyenne` qui prend en paramètre le nom du fichier csv et qui renvoie l'altitude minimun moyenne en France.
  
  En France, l'altitude minimum moyenne est de 193 m, retrouvez vous ce résultat  ?

* Ecrire une fonction `habitant_moyenne_2012` qui prend en paramètre le nom du fichier csv et qui renvoie le nombre d'habitant par ville en moyenne et en 2012.

* Ecrire une fonction `habitant_altitude_min_moyenne`  qui prend en paramètre le nom du fichier csv et une altitude et qui renvoie le nombre moyen d'habitants en 2012 dans une ville ayant une altitude minimum égale à la valeur passée en paramètre. 
  
  Vous devriez constater que les villes ayant une altitude minimum supérieure à 1500 m avaient en moyenne 350 habitants en 2012.
