import requests
import json
import folium

call = requests.get("http://api.open-notify.org/astros.json")
file = call.text

with open("astros.json", "w") as f:
    f.write(file)
    
with open("astros.json", "r") as f:
    data = json.load(f)
    
astros_name = []
for astros in data["people"]:
    if astros['craft'] == "ISS":
        astros_name.append(astros['name'])
print("Les personnes à bord de l'ISS sont", astros_name)

call2 = requests.get("http://api.open-notify.org/iss-now.json")
file2 = call2.text

with open("position.json", 'w') as f:
    f.write(file2)
    
with open("position.json", "r") as f:
    data2 = json.load(f)
    
pos = data2["iss_position"]
position = (float(pos["latitude"]), float(pos["longitude"]))
print("La position de l'ISS est : latitude:", position[0], ", longitude:", position[1])

folium_map = folium.Map(location=position, zoom_start = 3)
folium.Marker(position, popup = "Position de l'ISS").add_to(folium_map)
folium_map.save('position_iss.html')