import csv

def lecture(fichier_csv) :
    with open(fichier_csv, "r", encoding='utf-8') as csvfich:
        reader = csv.DictReader(csvfich)
        data = [dict(ligne) for ligne in reader]
        return data

def liste_villes(fichier_csv):
    return [villes['nom'] for villes in lecture(fichier_csv)]

def liste_villes_altitude(fichier_csv, altitude):
    return [villes['nom'] for villes in lecture(fichier_csv) if villes['alt_min'] != 'NULL' and int(villes['alt_min']) >= altitude]

def liste_villes_altitude_max(fichier_csv, altitude):
    return [villes['nom'] for villes in lecture(fichier_csv) if villes['alt_min'] != 'NULL' and int(villes['alt_max']) >= altitude]

def densite_max(fichier_csv, densite):
    return [villes['nom'] for villes in lecture(fichier_csv) if int(villes['dens']) <= densite]

def altitude_densite(fichier_csv, altitude, densite):
    return [villes['nom'] for villes in lecture(fichier_csv) if int(villes['dens']) <= densite and villes['alt_min'] != 'NULL' and int(villes['alt_min']) >= altitude]

def altitude_min_moyenne(fichier_csv):
    altitude = 0
    n = 0
    for villes in lecture(fichier_csv):
        if villes['alt_min'] != 'NULL':
            altitude = altitude + int(villes['alt_min'])
            n += 1
    return altitude / n

def habitant_moyenne_2012(fichier_csv):
    habitants = 0
    n = 0
    for villes in lecture(fichier_csv):
        habitants = habitants + int(villes['nb_hab_2012'])
        n += 1
    return habitants / n

def habitant_altitude_min_moyenne(fichier_csv, altitude):
    habitants = 0
    n = 0
    for villes in lecture(fichier_csv):
        if villes['alt_min'] != 'NULL' and int(villes['alt_min']) >= altitude:
            habitants = habitants + int(villes['nb_hab_2012'])
            n += 1
    return habitants / n