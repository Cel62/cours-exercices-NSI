import csv

def lecture(fichier_csv) :
    with open(fichier_csv, "r") as csvfich:
        reader = csv.DictReader(csvfich)
        data = [dict(ligne) for ligne in reader]
        return data

donnees = lecture('country-capitals_mini.csv')
