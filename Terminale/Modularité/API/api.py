import requests
import folium
import json

#Couleurs utilisées pour le zonage
tab_couleur = ["#0e7c0a", "#c1ff00", "#e1d219","#e1ba19", "#e17d19", "#ff0000"]

#latitude, longitude du point d'origine
coord_origine = (50.720184,1.617054)
api_key = '5b3ce3597851110001cf624843c630f967984e56b4f5c900358f474b'

#Temps max pour l'analyse des isochrones en secondes : 30 minutes = 1800 s
temps_max = 1800

#Intervalle de temps pour l'analyse des isochrones en secondes : 5 minutes = 300 s
intervalle_temps = 300

#Mode piéton
profile = 'foot-walking'

#Coordonnées du point d'origine (long,lat)
coord_ori = (coord_origine[1],coord_origine[0])

#Elaboration du fichier JSON de paramétrage
body = {"locations":[coord_ori],
        "range":[temps_max],
        "attributes":["area"],
        "interval":intervalle_temps,
        "location_type":"start","range_type":"time"
        }

#Elaboration de l'entête de la requête avec la clé API
headers = {
            'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
            'Authorization': api_key
        }

#Elaboration de la requête html
url = 'https://api.openrouteservice.org/v2/isochrones/'+ profile
call = requests.post(url,json=body, headers=headers)

#Affichage code réponse + message
print(call.status_code, call.reason)

#Enregistrement du texte JSON de la requête dans un fichier JSON
geo = call.text
with open('data.json', 'w') as f:
    f.write(geo)
    
#Lecture du fichier enregistré (pour être dans le bon type ensuite)
with open('data.json', 'r') as f:
    data = json.load(f)

#Création de la carte centrée sur le point d'origine
folium_map = folium.Map(location=coord_origine, zoom_start = 14)
folium.Marker(coord_origine, popup = "Lieu de travail").add_to(folium_map)

#Exploitation du fichier JSON
i=0
for zone in data["features"]:
    valeur_temps = zone["properties"]["value"]
    print(valeur_temps)
    #Création de liste contenant les points de passage dans l'ordre
    path_list = [(y, x) for x, y in zone["geometry"]["coordinates"][0]]
    folium.Polygon(path_list,color=tab_couleur[i]).add_to(folium_map)
    i += 1
    
#Enregistrement de la carte
folium_map.save('map_maison.html')