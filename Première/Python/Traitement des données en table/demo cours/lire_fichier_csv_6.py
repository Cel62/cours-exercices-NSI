import csv
fichier = open("country-capitals_mini.csv", "r")

reader = csv.DictReader(fichier)
pays = [dict(ligne) for ligne in reader]  # création d'une liste par compréhension

fichier.close()
