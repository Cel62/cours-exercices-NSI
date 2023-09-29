# Traitement des données en tables

### Introduction

Les données en informatique sont de plus en plus nombreuses, elles doivent être stockées et pouvoir être gérées, partagées ou modifiées à distance.

La recherche sur des systèmes offrant ces possibilités date du début des années 1960 en particulier avec les missions Apollo. Des sociétés comme IBM et Rockwell travaillaient alors sur des systèmes de gestion de base de données (SGBD) où les informations ne sont plus stockées de manière hiérarchique comme une arborescence de fichiers.

L'objectif de ce chapitre est d'introduire la notion de base de données en utilisant des données disposées en tables (à l'image d'un tableur).

Exemples de sources de fichiers  : 

* [https://www.ined.fr/fr/tout-savoir-population/chiffres/tous-les-pays-du-monde/](https://www.ined.fr/fr/tout-savoir-population/chiffres/tous-les-pays-du-monde/)

* [https://www.insee.fr/fr/statistiques/3677785?sommaire=3677855](https://www.insee.fr/fr/statistiques/3677785?sommaire=3677855)

* [https://www.data.gouv.fr/fr/datasets/codes-postaux/](https://www.data.gouv.fr/fr/datasets/codes-postaux/)

* [https://opendata.lillemetropole.fr/explore/dataset/vlille-realtime/information/](https://opendata.lillemetropole.fr/explore/dataset/vlille-realtime/information/)

* [Les données relatives au COVID-19 en France - data.gouv.fr](https://www.data.gouv.fr/fr/pages/donnees-coronavirus)

Un exemple d'utilisation des données liées au covid : [https://covidtracker.fr/]()

### Notion de fichier CSV

Nous allons utiliser un tableau issu du site [Techslides.com](http://techslides.com/list-of-countries-and-capitals) regroupant toutes les capitales des pays et leurs coordonnées GPS.

Vous trouvez ci-dessous un aperçu (il y a en réalité 245 pays) de ce tableau dans un tableur :

![](C:\Users\frede\OneDrive%20-%20ac-lille.fr\Travail%20(Cours)\NSI\Cours%20et%20TD\4%20-%20Traitement%20des%20données%20en%20table\image_donnes.png)

Ces informations sont regroupées sous la forme d'un fichier texte où les données sur chaque ligne sont séparées par une virgule (cela peut aussi être un point-virgule, une tabulation ou un autre caractère).

Pour ce cours, nous utiliserons une version allégée `country-capitals_mini.csv`  avec seulement quelques pays. A la fin du cours, des activités vous seront proposées en utilisant le fichier complet `country-capitals.csv`.

```python
CountryName,CapitalName,CapitalLatitude,CapitalLongitude,CountryCode,ContinentName
France,Paris,48.86666666666667,2.333333,FR,Europe
French Polynesia,Papeete,-17.533333333333335,-149.566667,PF,Australia
Gabon,Libreville,0.38333333333333336,9.450000,GA,Africa
The Gambia,Banjul,13.45,-16.566667,GM,Africa
Georgia,Tbilisi,41.68333333333333,44.833333,GE,Europe
Germany,Berlin,52.516666666666666,13.400000,DE,Europe
Ghana,Accra,5.55,-0.216667,GH,Africa
Gibraltar,Gibraltar,36.13333333333333,-5.350000,GI,Europe
Greece,Athens,37.983333333333334,23.733333,GR,Europe
```

Un tel fichier est au format CSV (comma-separated values) qui est un moyen simple d'échanger des données, dans ce format :

* les fichiers CSV sont de simples fichiers textes ;

* chaque ligne du fichier correspond à une ligne de la table ;

* chaque ligne est séparée en champs au moyen du caractère "," (pas d'espace autour des virgules) ;

* toutes les lignes du fichier ont le même nombre de champs ;

* la première ligne peut représenter des noms d'attributs ou commencer directement avec les données ;

* on peut utiliser des guillemets droits " " pour délimiter le contenu des champs

* un champ contenant un retour à la ligne, une virgule ou des guillements droits doit obligatoirement être entre guillemets droits ;

* un guillemet droit utilisé comme caractère (et non comme délimiteur) doit être doublé.

<u>Pour aller plus loin :</u> [Infolabs.io - Comment produire un fichier CSV de qualité](https://infolabs.io/sites/default/files/files/comment_produire_un_fichier_csv_de_qualite_1.1.pdf)

### Lire un fichier csv

Pour lire le contenu d'un fichier CSV sous la forme d'une liste composé de listes, le code minimal est le suivant :

```python
# voir étapes 1, 2 et 3
fichier = open("country-capitals_mini.csv", "r")

for ligne in fichier:
    donnees = ligne.rstrip().split(',')      
    print(donnees)                                

fichier.close()
```

**Remarque :** 

* open() permet d'ouvrir le fichier CSV ici en lecture "r" = read

* rstrip() permet d'enlever le dernier caractère de chaque ligne qui correspond au saut de ligne avec "\n" 

* split(",") permet de renvoyer une liste de mots séparés par le caractère ","

* close() permet de fermer le fichier et ainsi de libérer les ressources systèmes utilisées.

on obtient une table sous forme d'une liste (de listes) :

```python
['CountryName', 'CapitalName', 'CapitalLatitude', 'CapitalLongitude', 'CountryCode', 'ContinentName']
['France', 'Paris', '48.86666666666667', '2.333333', 'FR', 'Europe']
['French Polynesia', 'Papeete', '-17.533333333333335', '-149.566667', 'PF', 'Australia']
['Gabon', 'Libreville', '0.38333333333333336', '9.450000', 'GA', 'Africa']
['The Gambia', 'Banjul', '13.45', '-16.566667', 'GM', 'Africa']
['Georgia', 'Tbilisi', '41.68333333333333', '44.833333', 'GE', 'Europe']
['Germany', 'Berlin', '52.516666666666666', '13.400000', 'DE', 'Europe']
['Ghana', 'Accra', '5.55', '-0.216667', 'GH', 'Africa']
['Gibraltar', 'Gibraltar', '36.13333333333333', '-5.350000', 'GI', 'Europe']
['Greece', 'Athens', '37.983333333333334', '23.733333', 'GR', 'Europe']
```

**Remarque :** la première liste contient la liste des champs (noms des colonnes).

On peut utiliser la bibliothèque `csv` qui simplifiera la lecture d'un fichier csv :

```python
# voir étape 4
import csv
fichier = open("country-capitals_mini.csv", "r")

reader = csv.reader(fichier)

for ligne in reader:
    print(ligne)

fichier.close()
```

Remarque :

* la première ligne permet l'import du module `csv`

* ensuite nous ouvrons le fichier en lecture (fonction open avec le paramètre "r" pour read)
- nous initialisons le lecteur (reader) de ce fichier csv

- l'instruction `for ligne in reader` va alors permettre d'énumérer les différentes lignes de notre fichier csv

- la variable ligne contient à chaque itération une ligne du fichier sous forme de liste

- on termine le programme en fermant le fichier ouvert en lecture.

### Plus loin avec le module csv

Si nous utilisons le module csv, c'est qu'il permet de faciliter l'écriture de nos programmes, dans l'exemple précédent nous n'avons pas vraiment tenu compte de l'entête de notre fichier (la première ligne).

Nous allons voir ici, qu'il est possible pour chacune des données de notre fichier, de créer un dictionnaire qui va nous permettre d'identifier plus facilement nos informations.

L'idée étant d'obtenir un format de donnée comme celui-ci :

```python
{'CountryName': 'France', 'CapitalName': 'Paris', 'CapitalLatitude': '48.86666666666667', 'CapitalLongitude': '2.333333', 'CountryCode': 'FR', 'ContinentName': 'Europe'}
```

Voici le programme python correspondant :

```python
# voir étape 5
import csv
fichier = open("country-capitals_mini.csv", "r")

reader = csv.DictReader(fichier)

for ligne in reader:
    print(dict(ligne))

fichier.close()
```

Nous avons remplacé le lecteur (reader) de base par un lecteur avec création automatique de dictionnaire (DictReader). Celui-ci va permettre, comme dans la version précédente de lire le fichier ligne par ligne mais en faisant le lien avec la ligne d'entête !

A l'exécution de ce programme nous obtenons donc :

```python
{'CountryName': 'France', 'CapitalName': 'Paris', 'CapitalLatitude': '48.86666666666667', 'CapitalLongitude': '2.333333', 'CountryCode': 'FR', 'ContinentName': 'Europe'}
{'CountryName': 'French Polynesia', 'CapitalName': 'Papeete', 'CapitalLatitude': '-17.533333333333335', 'CapitalLongitude': '-149.566667', 'CountryCode': 'PF', 'ContinentName': 'Australia'}
{'CountryName': 'Gabon', 'CapitalName': 'Libreville', 'CapitalLatitude': '0.38333333333333336', 'CapitalLongitude': '9.450000', 'CountryCode': 'GA', 'ContinentName': 'Africa'}
{'CountryName': 'The Gambia', 'CapitalName': 'Banjul', 'CapitalLatitude': '13.45', 'CapitalLongitude': '-16.566667', 'CountryCode': 'GM', 'ContinentName': 'Africa'}
{'CountryName': 'Georgia', 'CapitalName': 'Tbilisi', 'CapitalLatitude': '41.68333333333333', 'CapitalLongitude': '44.833333', 'CountryCode': 'GE', 'ContinentName': 'Europe'}
{'CountryName': 'Germany', 'CapitalName': 'Berlin', 'CapitalLatitude': '52.516666666666666', 'CapitalLongitude': '13.400000', 'CountryCode': 'DE', 'ContinentName': 'Europe'}
{'CountryName': 'Ghana', 'CapitalName': 'Accra', 'CapitalLatitude': '5.55', 'CapitalLongitude': '-0.216667', 'CountryCode': 'GH', 'ContinentName': 'Africa'}
{'CountryName': 'Gibraltar', 'CapitalName': 'Gibraltar', 'CapitalLatitude': '36.13333333333333', 'CapitalLongitude': '-5.350000', 'CountryCode': 'GI', 'ContinentName': 'Europe'}
{'CountryName': 'Greece', 'CapitalName': 'Athens', 'CapitalLatitude': '37.983333333333334', 'CapitalLongitude': '23.733333', 'CountryCode': 'GR', 'ContinentName': 'Europe'}
```

On constate que la ligne d'entête n'apparait pas dans la liste mais a été utilisée pour créer les clés des dictionnaires.

### Stocker les données/dictionnaire dans une liste

Dans la pratique, on mémorise les données du fichier dans une liste :

```python
# voir étape 6
import csv
fichier = open("country-capitals_mini.csv", "r")

reader = csv.DictReader(fichier)
pays = [dict(ligne) for ligne in reader]

fichier.close()
```

`pays` est donc une liste de nos enregistrements :

```python
>>> pays
[{'CountryName': 'France', 'CapitalName': 'Paris', 'CapitalLatitude': '48.86666666666667', 'CapitalLongitude': '2.333333', 'CountryCode': 'FR', 'ContinentName': 'Europe'}, {'CountryName': 'French Polynesia', 'CapitalName': 'Papeete', 'CapitalLatitude': '-17.533333333333335', 'CapitalLongitude': '-149.566667', 'CountryCode': 'PF', 'ContinentName': 'Australia'}, {'CountryName': 'Gabon', 'CapitalName': 'Libreville', 'CapitalLatitude': '0.38333333333333336', 'CapitalLongitude': '9.450000', 'CountryCode': 'GA', 'ContinentName': 'Africa'}, {'CountryName': 'The Gambia', 'CapitalName': 'Banjul', 'CapitalLatitude': '13.45', 'CapitalLongitude': '-16.566667', 'CountryCode': 'GM', 'ContinentName': 'Africa'}, {'CountryName': 'Georgia', 'CapitalName': 'Tbilisi', 'CapitalLatitude': '41.68333333333333', 'CapitalLongitude': '44.833333', 'CountryCode': 'GE', 'ContinentName': 'Europe'}, {'CountryName': 'Germany', 'CapitalName': 'Berlin', 'CapitalLatitude': '52.516666666666666', 'CapitalLongitude': '13.400000', 'CountryCode': 'DE', 'ContinentName': 'Europe'}, {'CountryName': 'Ghana', 'CapitalName': 'Accra', 'CapitalLatitude': '5.55', 'CapitalLongitude': '-0.216667', 'CountryCode': 'GH', 'ContinentName': 'Africa'}, {'CountryName': 'Gibraltar', 'CapitalName': 'Gibraltar', 'CapitalLatitude': '36.13333333333333', 'CapitalLongitude': '-5.350000', 'CountryCode': 'GI', 'ContinentName': 'Europe'}, {'CountryName': 'Greece', 'CapitalName': 'Athens', 'CapitalLatitude': '37.983333333333334', 'CapitalLongitude': '23.733333', 'CountryCode': 'GR', 'ContinentName': 'Europe'}]
```

Nous pouvons regrouper le code sous forme d'une fonction `lecture_csv` qui prend en paramètre le nom du fichier csv et qui retourne les données sous forme d'une liste de dictionnaires :

```python
# voir étape 7
import csv

def lecture(fichier_csv):
    fichier = open(fichier_csv, "r")
    reader = csv.DictReader(fichier)
    data = [dict(ligne) for ligne in reader]
    fichier.close()
    return data
```

**Astuce :** ci-dessous une amélioration pour éviter d'oublier de fermer le fichier en utilisant `with` et `as` pour gérer l'ouverture d'un fichier csv :

```python
# voir étape 7 bis
import csv

def lecture(fichier_csv) :
    with open(fichier_csv, "r") as csvfich:
        reader = csv.DictReader(csvfich)
        data = [dict(ligne) for ligne in reader]
        return data
```

### Extraire des données suivant certains critères.

Pour cela on peut utiliser les listes en compréhension.

**Exemple n°1 :** accéder aux données extraites

```python
# tous les exemples ci-dessous sont dans étape 8
# afficher l'item d'index 5

>>> donnees[5]
{'CountryName': 'Germany', 'CapitalName': 'Berlin', 'CapitalLatitude': '52.516666666666666', 'CapitalLongitude': '13.400000', 'CountryCode': 'DE', 'ContinentName': 'Europe'}

# afficher le pays correspondant
>>> donnees[5]['CountryName']
'Germany'

# afficher le code du pays correspondant
>>> donnees[5]['CountryCode']
'DE'
```

**Exemple n°2 :** extraire la liste des pays

```python
liste_pays = [pays['CountryName'] for pays in donnees]

>>> liste_pays
['France', 'French Polynesia', 'Gabon', 'The Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece']
```

**Exemple n°3 :** extraire la liste des pays et leurs codes sous forme de tuples

```python
liste_pays_code = [(pays['CountryName'], pays['CountryCode']) for pays in donnees]

>>> liste_pays_code
[('France', 'FR'), ('French Polynesia', 'PF'), ('Gabon', 'GA'), ('The Gambia', 'GM'), ('Georgia', 'GE'), ('Germany', 'DE'), ('Ghana', 'GH'), ('Gibraltar', 'GI'), ('Greece', 'GR')]
```

**Exemple n°4 :** extraire la liste des pays européen

```python
liste_pays_europe = [pays['CountryName'] for pays in donnees if pays['ContinentName'] == 'Europe']

>>> liste_pays_europe
['France', 'Georgia', 'Germany', 'Gibraltar', 'Greece']
```

**Exemple n°5 :** extraire la liste des pays en europe avec leur code sous forme d'une liste de tuple

```python
liste_pays_europe_code = [(pays['CountryName'], pays['CountryCode']) for pays in donnees if pays['ContinentName'] == 'Europe']

>>> liste_pays_europe_code
[('France', 'FR'), ('Georgia', 'GE'), ('Germany', 'DE'), ('Gibraltar', 'GI'), ('Greece', 'GR')]
```

**Exemple n°6 :** extraire la liste des pays de l'hémisphère sud

```python
liste_pays_sud = [pays['CountryName'] for pays in donnees if float(pays['CapitalLatitude']) <= 0]

>>> liste_pays_sud
['French Polynesia']
```

### Activités

Ouvrir le fichier `activites_tables.py` afin de réaliser les activités ci-dessous.

* s'approprier le cours en utilisant cette fois ci le fichier csv complet `country-capitals.csv`  et en refaisant les exemples présentés ci-dessus.

* Réaliser les extractions suivantes en complétant le fichier fourni :
  
  * Créer une fonction `asie` sans paramètre qui renvoie la liste des pays du continent asiatique (en déduire le nombre de pays sur le continent asiatique).
  
  * Créer une fonction `continent` qui renvoie la liste des pays d'un continent donné en paramètre.
  
  * Créer une fonction `capitale` qui renvoie la capitale d'un pays passée en paramètre.
  
  * Créer une fonction `coordo_capitale` qui renvoie un tuple (n-uplet) des coordonnées GPS de la capitale d'un pays passée en paramètre.
  
  * Créer une fonction `liste_pays_premiere_lettre` qui renvoie la liste des pays qui commence par une lettre donnée en paramètre.

* Créer une fonction qui crée une page html sur laquelle on trouvera la capitale du pays donné en paramètre. On utilisera pour cela la bibliothèque `folium`, vous trouverez ci-dessous un exemple d'utilisation :
  
  ```python
  import folium
  carte = folium.Map(location=[ 43.6000, 1.433333])
  carte.save('maCarte.html')
  ```

Plus d'informations sur la bibliothèque `folium` : [https://python-visualization.github.io/folium/quickstart.html](https://python-visualization.github.io/folium/quickstart.html)

Pour les plus avancés, utiliser la bibliothèque `webbrowser` afin d'obtenir l'ouverture de la carte créée sous forme de page html au lancement de la fonction.
