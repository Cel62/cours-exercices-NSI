import csv
fichier = open("country-capitals_mini.csv", "r")

reader = csv.DictReader(fichier)

for ligne in reader:
    print(dict(ligne))

fichier.close()
