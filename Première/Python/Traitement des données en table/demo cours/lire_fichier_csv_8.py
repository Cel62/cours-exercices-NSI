import csv

def lecture(fichier_csv) :
    with open(fichier_csv, "r") as csvfich:
        reader = csv.DictReader(csvfich)
        data = [dict(ligne) for ligne in reader]
        return data

donnees = lecture('country-capitals_mini.csv')

# utiliser la liste de dictionnaire
# afficher l'item d'index 5
print('item n°5 :', donnees[5])
# afficher le pays correspondant
print('le pays n°5 est :', donnees[5]['CountryName'])
# afficher le code du pays correspondant
print('le code du pays n°5 :', donnees[5]['CountryCode'])

# extraire la liste des pays
liste_pays = [pays['CountryName'] for pays in donnees]

# extraire la liste des pays et leurs codes sous forme de tuples
liste_pays_code = [(pays['CountryName'], pays['CountryCode']) for pays in donnees]

# extraire la liste des pays en europe avec leur code sous forme d'une liste de tuple
liste_pays_europe = [pays['CountryName'] for pays in donnees if pays['ContinentName'] == 'Europe']

# extraire la liste des pays en europe avec leur code sous forme d'une liste de tuple
liste_pays_europe_code = [(pays['CountryName'], pays['CountryCode']) for pays in donnees if pays['ContinentName'] == 'Europe']

# extraire la liste des pays de l'hémisphére sud
liste_pays_sud = [pays['CountryName'] for pays in donnees if float(pays['CapitalLatitude']) <= 0]