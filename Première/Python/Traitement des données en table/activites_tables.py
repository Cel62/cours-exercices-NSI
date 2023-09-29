import csv
import folium
import webbrowser

def lecture(fichier_csv) :
    with open(fichier_csv, "r") as csvfich:
        reader = csv.DictReader(csvfich)
        data = [dict(ligne) for ligne in reader]
        return data

donnees = lecture('country-capitals.csv')

# Créer une fonction qui renvoie la liste des pays du continent asiatique
def asie():
    return [pays['CountryName'] for pays in donnees if pays['ContinentName'] == 'Asia']

# Créer une fonction qui renvoie la liste des pays d'un continent donné en paramètre
def continent(country):
    return [pays['CountryName'] for pays in donnees if pays['ContinentName'] == country]
        
# Créer une fonction qui renvoie la capitale d'un pays
def capitale(country):
    return [pays['CapitalName'] for pays in donnees if pays['CountryName'] == country]
        
# Créer une fonction qui renvoie un tuple des coordonnées de la capitale d'un pays
def coordo_capitale(country):
    for pays in donnees:
        if pays['CountryName'] == country:
            return (pays['CapitalLatitude'], pays['CapitalLongitude'])
        
# Créer une fonction qui renvoie la liste des pays qui commence par une lettre donnée en paramètre
def liste_pays_premiere_lettre(lettre):
    liste_pays = []
    for pays in donnees:
        if pays['CountryName'][0] == lettre:
            liste_pays.append(pays['CountryName'])
    return liste_pays
            
        
# Créer une fonction qui crée une page html sur laquelle on trouvera la capitale du pays donné en paramètre. On utilisera pour cela la bibliothèque `folium`avec le code suivant :
def carte(country):
    carte = folium.Map(location = coordo_capitale(country), zoom_start = 50)
    folium.Marker(coordo_capitale(country), icon = folium.Icon(color='green')).add_to(carte)
    carte.save('maCarte.html')
    webbrowser.open("maCarte.html")