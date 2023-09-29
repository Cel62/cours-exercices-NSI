# Programme : donnees_exif.py
# Nom : Pihen
# Prénom : Céleste
# version 1 créée le 12/01/2023 en NSI

from PIL import Image             # import du module Image de la bibliothèque PIL = Pillow
from PIL.ExifTags import TAGS, GPSTAGS
import folium
import webbrowser

def get_exif(fichier):
    img = Image.open(fichier)
    exif_data = img._getexif()
    return exif_data

def get_exif_format(fichier):
    exif_data = get_exif(fichier)
    exif_format = {}
    for cle, valeur in exif_data.items():
        exif_format[TAGS[cle]] = valeur
    return exif_format
    
def get_gps(fichier):
    info_gps = get_exif_format(fichier)
    return info_gps['GPSInfo']

def get_gps_format(fichier):
    gps_data = get_gps(fichier)
    gps_format = {}
    for cle, valeur in gps_data.items():
        gps_format[GPSTAGS[cle]] = valeur
    return gps_format

def affichage_carte(fichier):
    gps_data = get_gps_format(fichier)
    latitude = gps_data["GPSLatitude"][0][0] + gps_data["GPSLatitude"][1][0] / 60 + gps_data["GPSLatitude"][2][0] / 3600
    longitude = gps_data["GPSLongitude"][0][0] + gps_data["GPSLongitude"][1][0] / 60 + gps_data["GPSLongitude"][2][0] / 3600
    
    if gps_data["GPSLatitudeRef"] == "S":
        latitude = -latitude
    if gps_data["GPSLongitudeRef"] == "W":
        longitude = -longitude
    
    carte = folium.Map(location = (latitude, longitude), zoom_start = 50)
    folium.Marker((latitude, longitude), icon = folium.Icon(color='green')).add_to(carte)
    carte.save('maCarte.html')
    webbrowser.open("maCarte.html")