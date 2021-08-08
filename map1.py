import folium 
import pandas

df = pandas.read_csv("mapping/Volcanoes.txt")
lon = list(df["LON"])
lat = list(df["LAT"])
elev = list(df["ELEV"])

html = """"<h4> Volcano Information:</h4> Height: %s m"""
map = folium.Map(location = [38.58, -99.09], zoom_start = 6, tiles = "Stamen Terrain")

fgv = folium.FeatureGroup(name = "Volcanoes")

#for i,j in zip([1,2,3],[4,5,6]): FUNCTIONALITY OF THE ZIP FUNCTION 
#...     print(i,"and",j)
#...                    
#1 and 4
#2 and 5
#3 and 6


#for coordinates in [[38.58, -99.09],[37.50, -96.05]]:

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


for lt,ln,ele in zip(lat,lon,elev):
    #fg.add_child(folium.Marker(location= [lt,ln], zoom_start =8 , popup=ele, icon=folium.Icon(color = color_producer(ele),icon= 'Circle',prefix= 'fa')))
    fgv.add_child(folium.CircleMarker(location= [lt,ln], radius = 6, popup=str(ele), fill_color = color_producer(ele), color= 'grey', fill_opacity= 0.7))


fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = (open('mapping/world.json','r', encoding = 'utf-8-sig').read() ),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000  else 'red'}))



fl = folium.LayerControl()
map.add_child(fgv)
map.add_child(fgp)
map.add_child(fl)


map.save("Map2.html")