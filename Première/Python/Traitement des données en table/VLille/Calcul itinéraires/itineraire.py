import folium
import webbrowser
from pyroutelib3 import Router

# latitude et longitude du point de départ (en décimal)
lat1=
lon1=

# latitude et loogitude du point d'arrivéè (en décimal)
lat2=
lon2=

router = Router("foot")
depart = router.findNode(lat1, lon1)
arrivee = router.findNode(lat2,  lon2)
status, route = router.doRoute(depart, arrivee)

if status == 'success':
    routeLatLons = list(map(router.nodeLatLon, route))
    
c= folium.Map(location=[lat1, lon1],zoom_start=12)
for indice,coord in enumerate(routeLatLons):
    if indice%10==0:
        coord=list(coord)
        folium.CircleMarker(coord, radius = 3,fill=True, color='red').add_to(c)
        
folium.Marker((lat1,lon1),popup="Départ").add_to(c)
folium.Marker((lat2,lon2),popup="Arrivée").add_to(c)
folium.PolyLine(routeLatLons, color="blue", weight=2.5, opacity=1).add_to(c)

c.save('maCarte_2.html')
webbrowser.open('maCarte_2.html')