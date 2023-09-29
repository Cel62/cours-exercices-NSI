fichier = open("country-capitals_mini.csv", "r")

for ligne in fichier:
    print(ligne.split(','))

fichier.close()