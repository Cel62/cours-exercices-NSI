import sqlite3
fichiersDonnees = "personne.db"
connection = sqlite3.connect(fichiersDonnees)

cur = connection.cursor()

cur.execute("SELECT * FROM personne;")
personnes = cur.fetchall() # récupère toutes les personnes
print(personnes)

# le nom et le prénom de ces personnes :
for personne in personnes:
    print(personne[0], personne[1])

connection.close()