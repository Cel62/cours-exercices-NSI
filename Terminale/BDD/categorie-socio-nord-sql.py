import sqlite3
fichiersDonnees = "categories-socio-nord.db"
connection = sqlite3.connect(fichiersDonnees)

cur = connection.cursor()

cur.execute("SELECT AVG(effectif) AS total FROM evolution WHERE genre='Femmes'")
nb_femmes_nord = cur.fetchone()
print(nb_femmes_nord)

connection.close()