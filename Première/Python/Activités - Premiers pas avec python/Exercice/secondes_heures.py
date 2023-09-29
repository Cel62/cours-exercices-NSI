secondes = int(input("Entrez un nombre de seconde(s)."))

if secondes < 60:
    print("Le nombre de seconde(s) est", secondes)
elif secondes < 3600 and secondes > 60:
    print("Minute(s) :", secondes//60, ", Seconde(s) :", secondes%60)
elif secondes >= 3600:
    print("Heure(s) :", secondes//3600, ", Minute(s) :", secondes%3600//60, ", Seconde(s) :", secondes%60)