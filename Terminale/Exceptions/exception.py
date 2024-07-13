class TestException(Exception):
    pass

annee = input() # L'utilisateur saisit l'année
try:
    annee = int(annee) # On tente de convertir l'année
    if annee <= 0:
        raise TestException()
except TestException:
    print("La valeur saisie est invalide (l'année est peut-être négative).")