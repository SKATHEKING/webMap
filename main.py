
import folium
import pandas

#create dataframe
data = pandas.read_csv('smallerCities.csv')
lat = data['lat']
lon = data['lng']
#standard map
map = folium.Map(location=[80, -100], zoom_start=6, tiles='Stamen Terrain')
map.add_child(folium.Marker(location=[51.495830636464845, -0.06866273746874785], popup='this place is marked', icon=folium.Icon(color='green')))
map.save('mapStandard.html')

# map of london
ukMap = folium.Map(location=[51.495830636464845, -0.06866273746874785], zoom_start=6, tiles='Stamen Terrain')
for lt, ln in zip(lat, lon):
    map.add_child(folium.Marker(location=[lt, ln], popup='this place is marked', icon=folium.Icon(color='green')))
ukMap.save('mapUk.html')

