fichier = open("country-capitals_mini.csv", "r")

for ligne in fichier:
    donnees = ligne.split(',')      # convertit une chaîne en une liste de sous-chaînes en choisissant la virgule
                                    # comme caractère séparateur (sinon par défaut c'est l'espace)
    print(donnees)                                

fichier.close()