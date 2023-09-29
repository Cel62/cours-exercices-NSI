# Traitement des données en tables (tri et fusion)

## Tri d'une table

Lorsqu'on manipule des données en table, il est fréquent de vouloir les trier.

Si on reprend l'exercice 2 avec le fichier de données `villes.csv`, on peut par exemple vouloir afficher la liste des villes par ordre décroissant de leurs populations.

On utilisera pour cela les fonctionnalités de tri de python avec la fonction `sorted`.

La fonction `sorted` prend en argument un tableau (une liste) et renvoie une version triée **sous la forme d'un nouveau tableau** :

```python
>>> t = [21, 12, 34, 8, 45]
>>> sorted(t)
[8, 12, 21, 34, 45]
```

On peut remarquer que le tableau initial n'est pas modifié :

```python
>>> t
[21, 12, 34, 8, 45]
```

Cette fonction ne permet pas seulement le tri d'entiers, on peut aussi trier des chaînes de caractères qui se fera alors dans l'ordre alphabétique :

```python
>>> t = ['pomme', 'poire', 'banane', 'cerise', 'fraise']
>>> sorted(t)
['banane', 'cerise', 'fraise', 'poire', 'pomme']
```

La fonction `sorted` peut prendre des paramètres comme par exemple pour inverser l'ordre de tri :

```python
>>> sorted(t, reverse = True)

['pomme', 'poire', 'fraise', 'cerise', 'banane']
```

Plus d'informations : [https://docs.python.org/fr/3/howto/sorting.html](https://docs.python.org/fr/3/howto/sorting.html)

Si on essaye de trier le tableau contenant les villes avec le programme suivant :

```python
import csv

def lecture(fichier_csv) :
    with open(fichier_csv, 'r', encoding='utf-8') as csvfich:
        reader = csv.DictReader(csvfich)
        data = [dict(ligne) for ligne in reader]
        return data

donnees = lecture('villes.csv')

sorted(donnees)
```

On obtient :

```python
TypeError: '<' not supported between instances of 'dict' and 'dict'
```

Le message d'erreur nous indique que python ne sait pas trier des objets qui sont des dictionnaires. Pour utiliser la fonction `sorted` sur notre tableau de dictionnaires, il faut indiquer comment se ramener à des valeurs que python sait comparer (nombres, chaînes de caractères, n-uplets...).

Pour réaliser cela, on commence par définir une fonction qui prend en argument une ville (dans notre exemple) et qui renvoie la valeur que l'on souhaite utiliser pour notre tri :

```python
def population(x):
    return int(x['nb_hab_2012'])

liste = sorted(donnees, key = population)
```

La fonction `sorted` s'execute sur le tableau `donnees` en précisant qu'il faut utiliser la fonction `population` chaque fois que deux éléments doivent être comparés. On l'indique en passant le paramètre `key = population` à la fonction `sorted` .

<u>Remarque :</u> il faut utiliser `int` dans la fonction `population` car le champs `nb_hab_2012` est une chaîne de caractères dans le tableau.

### Activités sur les tris :

Les activités sont à rendre sous la forme d'un fichier `tri_table.py`.

> **Activités :**
> 
> Tester les différents exemples proposés ci-dessus.
> 
> Donner le code nécessaire pour obtenir la liste des villes triées par ordre alphabétique.
> 
> Donner la liste triée par ordre alphabétique de toutes les villes situées au nord de boulogne sur mer.
> 
>  Donner le code nécessaire pour obtenir la liste des villes triées par ordre d'altitude maximum décroissante.
> 
> Donner la liste triée par altitude décroissante des villes dont l'altitude maximum est de plus de 3000 m.

## Fusion de tables

Il est fréquent losqu'on travaille avec des données, de se retrouver avec plusieurs jeux de données. On peut alors se poser la question : "comment comniner les jeux de données en une seule table ?". Cette opération s'appelle une fusion de tables et nécessite quelques précautions particulières.

##### Réunion de tables

Une première opération naturelle est de vouloir mettre dans une même table les données de deux tables existantes (ou plus).

On trouve par exemple des fichiers CSV recensant les listes de prénoms nés dans certaines villes pour chaque année. 

Chaque année est stockée dans un fichiers CSV propre : Prénoms2007GF_Rennes.csv, Prénoms2008GF_Rennes.csv, Prénoms2009GF_Rennes.csv...

```csv
# début d'un fichier CSV avec les prénoms donnés en 2011
ANNAISS;MNAISS;CODCOM;LBCOM;SEXE;PRN;NBR
2011;35238;RENNES;FEMME;Manon;57
2011;35238;RENNES;FEMME;Louise;55
2011;35238;RENNES;FEMME;Chloé;50
2011;35238;RENNES;FEMME;Camille;42
```

Il est naturel de vouloir reunir tous ces jeux de données en un seul et ainsi pouvoir réaliser des opérations de tri ou encore des extractions.

Cette opération a du sens car tous ces fichiers et donc les tables correspondantes possèdent la même structure (les attributs ont les mêmes noms et sont en nombre identique) : ANNAISS, CODCOM, LBCOM, SEXE, PRN, NBR 

```python
import csv

def lecture(fichier_csv) :
    with open(fichier_csv, 'r', encoding='latin-1') as csvfich:
        reader = csv.DictReader(csvfich, delimiter=';')
        data = [dict(ligne) for ligne in reader]
        return data

prenom2014 = lecture('Prenoms2014GF_Rennes.csv')
prenom2015 = lecture('Prenoms2015GF_Rennes.csv')
prenom2014_2015 = prenom2014 + prenom2015
```

On obtient un nouveau tableau contenant les élèments de `prenom2014` suivis des élèments de `prenom2015`. Du point de vue de python cette opération est toujours autorisé mais dans le cadre de tables de données, il faut que les tables réunies aient les mêmes attributs.

##### Jointure de tables

On peut aller plus loin en considérant des tables ayant des attributs différents, mais au moins un attribut en commun.

Soit deux tables :

```csv
# liste_eleves.csv
Nom,Prénom,Année,e-mail
Galois,Evariste,2001,e.galois@yahoo.fr
Gauss,Carl,2000,c.gauss@yahoo.fr
Euler,Leonhard,2005,l.euler@yahoo.fr

# notes.csv
Nom,Maths,NSI,Anglais
Galois,17,14,17
Gauss,20,12,8 
Euler,19,15,13
```

On constate que ces deux tables ont comme attribut commun uniquement `Nom`.

L'idée est de fusionner ces deux tables pour obtenir :

```csv
Nom,Prénom,année,e-mail,Maths,NSI,Anglais
Galois,Evariste,2001,e.galois@yahoo.fr,17,14,17
Gauss,Carl,2000,c.gauss@yahoo.fr,20,12,8 
Euler,Leonhard,2005,l.euler@yahoo.fr,19,15,13
```

On commence par mettre le contenu des fichiers csv `liste_eleves.csv` et `notes.csv` sous forme de deux listes de dictionnaires :

```python
import csv

def lecture(fichier_csv) :
    with open(fichier_csv, 'r', encoding='utf-8') as csvfich:
        reader = csv.DictReader(csvfich)
        data = [dict(ligne) for ligne in reader]
        return data

liste = lecture('liste_eleves.csv')
notes = lecture('notes.csv')
```

On peut alors définir une fonction fusion qui prend en paramètre une ligne du tableau `liste` et une ligne du tableau `notes` et qui renvoie un dictionnaire contenant la fusion des deux lignes :

```python
def fusion(ligneA, ligneB):
    '''In : ligneA la table 1 (liste) et ligneB de la table 2 (notes)  
       Out : le dictionnaire fusion'''
    return {"Nom":ligneA["Nom"], "Prénom":ligneA["Prénom"],      
            "année":ligneA["Année"], "e-mail":ligneA["e-mail"],
            "Maths":ligneB["Maths"],"NSI":ligneB["NSI"],
            "Anglais":ligneB["Anglais"]}
```

On parcourt alors les deux tables `liste`et `notes` grâce à une boucle imbriquée et si une ligne de `liste` et une ligne de `notes` désigne le même `nom` , on appelle la fonction `fusion` afin d'ajouter le dictionnaire obtenu au tableau `jointure1` contenant les résultats des fusions :

```python
jointure1 = []
for ligneA in liste:
    for ligneB in notes:
        if ligneA['Nom'] == ligneB['Nom']:
            jointure1.append(fusion(ligneA, ligneB))
```

On peut travailler avec la création de liste par compréhension :

```python
jointure2 = [fusion(ligneA, ligneB) for ligneA in liste for ligneB in notes if ligneA['Nom'] == ligneB['Nom']]
```

Dans les deux cas, on obtient :

```python
[{'Nom': 'Galois', 'Prénom': 'Evariste', 'année': '2001', 'e-mail': 'e.galois@yahoo.fr', 'Maths': '17', 'NSI': '14', 'Anglais': '17'}, {'Nom': 'Gauss', 'Prénom': 'Carl', 'année': '2000', 'e-mail': 'c.gauss@yahoo.fr', 'Maths': '20', 'NSI': '12', 'Anglais': '8 '}, {'Nom': 'Euler', 'Prénom': 'Leonhard', 'année': '2005', 'e-mail': 'l.euler@yahoo.fr', 'Maths': '19', 'NSI': '15', 'Anglais': '13'}]
```

On peut alors générer un nouveau fichier `jointure.csv` :

```python
with open('jointure.csv', 'w', encoding='utf-8', newline="") as sortie:
        objet = csv.DictWriter(sortie,["Nom" ,"Prénom" ,"année",
        "e-mail" ,"Maths" ,"NSI" ,"Anglais"])

        # Pour écrire la ligne d'en têtes
        objet.writeheader()
        # On peut donner la table directement    
        objet.writerows(jointure1)
```

### Activité sur la reunion de tables :

Activité à rendre sous la forme d'un fichier nommé`reunion_tables.py`

> Reprendre l'exemple sur la réunion de deux tables comportant les prénoms donnés à Rennes en 2014 et 2015 et ajouter la table comportant les prénoms donnés en 2013.
> 
> Donner la liste des 3 prénoms les plus donnés (sans tenir compte de l'année) sur ces trois années en réalisant un tri sur la reunion des trois tables.

### Activités sur la jointure de tables :

Activités à rendre sous la forme d'un fichier nommé `jointure_tables.py`

> Reprendre les exemples sur la jointure de deux tables et les tester
> 
> Rendez-vous sur le site [https://donneespubliques.meteofrance.fr/?fond=produit&id_produit=94&id_rubrique=32](https://donneespubliques.meteofrance.fr/?fond=produit&id_produit=94&id_rubrique=32)  qui regroupe des données publiques de Météo France avec ici l'enneigement des stations de ski, consulter la documentation des jeux de données que l'on va utiliser.
> 
> Les jeux de données sont constitués de deux fichiers `stations.csv` et `donnees_meteo.csv` avec comme descripteur commun `numer_sta`, réaliser la jointure de ces deux tables avec comme descripteurs à garder (en modifiant leurs noms) :  "Latitude", "Longitude", "Altitude", "Hauteur_neige_altitude", "Hauteur_neige_fraiche.
> 
> Donner la liste des noms des stations avec plus de 0.4 m de neige en altitude.
