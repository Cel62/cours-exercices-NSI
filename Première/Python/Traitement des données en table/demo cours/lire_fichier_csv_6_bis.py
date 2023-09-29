import csv
def lecture(fichier_csv):
    with open(fichier_csv) as csvfich:
        reader = csv.DictReader(csvfich)
        data = [dict(ligne) for ligne in reader]
        return data
