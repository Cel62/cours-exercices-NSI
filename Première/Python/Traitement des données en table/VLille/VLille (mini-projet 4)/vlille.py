import csv
import folium
import webbrowser
from geopy import distance

def lecture(fichier_csv) :
    with open(fichier_csv, "r", encoding='utf-8') as csvfich:
        reader = csv.DictReader(csvfich, delimiter=';')
        data = [dict(ligne) for ligne in reader]
        return data

donnees = lecture('vlille-realtime.csv')

# Réalisez une fonction `velo_endroit` qui ne prend pas de paramètre et qui renvoie la liste des noms des dépôts de vélos
def velo_endroit():
    return [depots['nom'] for depots in donnees]

# Réalisez une fonction `velo_dispo` qui ne prend pas de paramètre et qui renvoie la liste des
# noms des endroits où se trouvent des vélos disponible.
def velo_dispo():
    return [depots['nom'] for depots in donnees if int(depots['nbVelosDispo']) > 0]

# Réalisez une fonction `velo_non_dispo` qui ne prend pas de paramètre et qui renvoie la liste des noms des endroits où il
# n'y plus de vélo disponible.
def velo_non_dispo():
    return [depots['nom'] for depots in donnees if int(depots['nbVelosDispo']) == 0]

# Réalisez une fonction `station_hs` qui ne prend pas de paramètre et qui renvoie la liste des noms des endroits où la station est hors service
def station_hs():
    return [depots['nom'] for depots in donnees if depots['etat'] == "HORS SERVICE"]

# Réalisez une fonction `info_depot` qui prend en paramètre le numéro du dépôt sous la forme d'un `identifiant` et qui retourne
# le nom du dépôt, son adresse (adresse + commune), le nombre de vélo disponible et la position sous forme d'un tuple (p-uplet)
def info_depot(identifiant):
    return [(depots['nom'], depots['adresse'], depots['commune'], depots['nbVelosDispo'], (float(depots['geo'].split(',')[0]), float(depots['geo'].split(',')[1]))) for depots in donnees if int(depots['ID']) == identifiant]

# Réalisez une fonction `recherche_station` qui prend en paramètre une chaine de caractère (en lettres majuscules) et
# qui renvoie une liste des dépôts (nom + ID) contenant cette chaîne
# ajout de la localisation
def recherche_station(chaine):
    return [(depots['nom'], depots['ID'], (float(depots['geo'].split(',')[0]), float(depots['geo'].split(',')[1]))) for depots in donnees if chaine in depots['nom']]

# Réalisez une fonction `recherche_station_carte` qui prend en paramètre une chaine de caractère (en lettres majuscules) et
# qui recherche les noms de dépôt contenant cette chaîne et les placent sur une carte avec des marqueurs
def recherche_station_carte(chaine):
    liste_station = recherche_station(chaine)
    carte = folium.Map(location = (50.633333, 3.066667), zoom_start = 13)
    for stations in liste_station:
        folium.Marker(stations[2], icon = folium.Icon(color='green')).add_to(carte)
    carte.save('maCarte.html')
    webbrowser.open("maCarte.html")

# Réalisez une fonction `dispo_proche` qui prend en paramètre l'identifiant d'un dépôt et qui renvoie la liste
# des dépôts situés à moins d'un kilomètre (à vol d'oiseau) où se trouve au moins un vélo de disponible.
# On utilisera la méthode `distance` du module `geopy`
def dispo_proche(identifiant, dist):
    pass