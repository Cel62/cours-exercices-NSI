somme = int(input("Rentrer une somme initiale."))
taux = int(input("Rentrer un taux d'intérêts annuel."))
annee = int(input("Rentrer un nombre d'années."))

montant = annee*(somme+(somme*taux/100))

print("Il y a", montant, "€ sur le livret après", année, "an(s).")