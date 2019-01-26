# The basemap
import folium
# location=[latitude,longitude]
# You can try other parameters from help(folium.Map)
map =folium.Map(location=[38.58,-99.09],zoom_start=2,tiles="Mapbox Bright")

# Adding points
# approach1
# map.add_child(folium.Marker(location=[38.2,-99.1],popup="HI I am a marker",icon = folium.Icon(color='green')))

# better approach2: better organized code
# fg = folium.FeatureGroup(name="My Map")

# fg.add_child(folium.Marker(location=[38.2,-99.1],popup="HI I am a marker",icon = folium.Icon(color='green')))
# multiple points from list
# for coordinates in [[36.2,-98.2],[38.6,-99.6]]:
#     fg.add_child(folium.Marker(location=coordinates,popup="HI I am a marker",icon = folium.Icon(color='green')))

# adding coordinatesfrom csv file
import pandas
data = pandas.read_csv("Volcanoes.txt")
latitude = list(data["LAT"])
longitude = list(data["LON"])
elevation =list(data["ELEV"])

# setting color of marker according to elevator range
def color_producer(elev):
    if elev < 1000:
        return 'green'
    elif 1000<=elev<3000:
        return 'orange'
    else:
        return 'pink'
fgv = folium.FeatureGroup(name="Volcanoes")

for lt,ln,el in zip(latitude,longitude,elevation):
    # fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+' m',icon = folium.Icon(color='green')))
    # fg.add_child(folium.Marker(location=[lt,ln],popup=str(el)+' m',icon = folium.Icon(color=color_producer(el)))
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius =6,popup=str(el)+' m',fill_color=color_producer(el),color='grey',fill = True,fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
#adding boundary to polygons
fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding = 'utf-8-sig').read(),
style_function= lambda x :{
'fillColor':'yellow' if x['properties']['POP2005']<10000000 else 'orange' if 1000000<=x['properties']['POP2005']<20000000 else 'red'
}))
# map.add_child(fg)
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
# Map to a html file to render the map
map.save("Map1.html")
# To find coordinates f  PARTICULAR place : maps.google.com
