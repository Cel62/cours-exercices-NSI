import sqlite3
connection = sqlite3.connect("categories-socio-nord.db")
cur = connection.cursor()

# cur.execute("SELECT evolution.code, correspondance.CodePostal, correspondance.Commune, evolution.categorie, evolution.genre, evolution.effectif FROM evolution INNER JOIN correspondance ON evolution.code = correspondance.CodeINSEE WHERE correspondance.COMMUNE = ?", ("VILLENEUVE-D'ASCQ",))
# 
# personnes = cur.fetchall()
# for p in personnes:
#     print(p)
    
def code_postal_where(cp):
    cur.execute("SELECT evolution.code, correspondance.CodePostal, correspondance.Commune, evolution.categorie, evolution.genre, evolution.effectif FROM evolution INNER JOIN correspondance ON evolution.code = correspondance.CodeINSEE WHERE correspondance.CodePostal = ?", (cp,))
    return cur.fetchall()

def code_postal(cp):
    cur.execute("SELECT evolution.code, correspondance.CodePostal, correspondance.Commune, evolution.categorie, evolution.genre, evolution.effectif FROM evolution INNER JOIN correspondance ON evolution.code = correspondance.CodeINSEE")
    resultat = cur.fetchall()
    resultat_final = []
    for r in resultat:
        if r[0] == cp:
            resultat_final.append(r)
    return resultat_final