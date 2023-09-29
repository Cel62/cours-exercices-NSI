fichier = open("country-capitals_mini.csv", "r")

for ligne in fichier:
    donnees = ligne
    print(donnees)

fichier.close()