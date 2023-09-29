import csv

def lecture(fichier_csv):
    with open(fichier_csv, "r") as csvfich:
        reader = csv.DictReader(csvfich)
        data = [dict(ligne) for ligne in reader]
        return data

identite = lecture('identite.csv')

def is_present(prenom):
    for identites in identite:
        if identites['prenom'] == prenom:
            return True
        return False

def date_naissance(nom):
    for identites in identite:
        if identites['nom'] == nom:
            return identites['date_naissance']