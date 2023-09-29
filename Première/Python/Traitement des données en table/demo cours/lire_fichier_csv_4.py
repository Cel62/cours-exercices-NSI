import csv
fichier = open("country-capitals_mini.csv", "r")

reader = csv.reader(fichier)

for ligne in reader:
    print(ligne)

fichier.close()