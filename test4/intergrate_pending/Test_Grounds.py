import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import json
import csv

geojson = json.load(open(r"C:\Users\Jongo\Downloads\SG_PlanZone_Geojson.json","r"))
#df_H = pd.read_csv(r"C:\Users\Jongo\source\repos\SG_HDB_Map\HDB_CSV.csv")

mapDic = {}

#Map for current 1 Mil Houses
df_C = pd.read_csv(r"C:\Users\Jongo\Downloads\Excel\percentage\UpdatedUserHse.csv")
for i in df_C["Area"]: #Fill dictionary with relevant data from CSV
    mapDic[i] = mapDic.get(i, 0) + 1    

with open('HeatMapFrameCurrent.csv', mode='w') as csvfile: #Write that data in new CSV
    fieldnames = ["Area","Count"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in mapDic:
        writer.writerow({"Area":i, "Count":mapDic[i]})


df_MC = pd.read_csv(r"C:\Users\Jongo\source\repos\SG_HDB_Map\Test_Grounds\HeatMapFrame.csv") #Open newly created CSV

for feature in geojson['features']: #Plot Map
    feature['id'] = feature['properties']['name']
fig = px.choropleth_mapbox(df_MC,
                           geojson=geojson,
                           color="Count",
                           locations="Area",
                           center={"lat": 1.3521, "lon": 103.8198},
                           mapbox_style="carto-positron",
                           zoom=10,
                           opacity=0.5,
                           title="Potential $1M HDB per area")

fig.show()

#fig.add_scattermapbox(lon = df_H['Long'],
#                      lat = df_H['Lat'],)

#Heat Map for past 1 Mil Houses
df_O = pd.read_csv(r"C:\Users\Jongo\Downloads\Excel\output\MillionDollarHse.csv")
for i in df_O["Location_Name"]: #Fill dictionary with relevant data from CSV
    mapDic[i] = mapDic.get(i, 0) + 1    

with open('HeatMapFrameOld.csv', mode='w') as csvfile: #Write that data in new CSV
    fieldnames = ["Area","Count"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in mapDic:
        writer.writerow({"Area":i, "Count":mapDic[i]})


df_MO = pd.read_csv(r"C:\Users\Jongo\source\repos\SG_HDB_Map\Test_Grounds\HeatMapFrame2.csv") #Open newly created CSV

for feature in geojson['features']: #Plot Map
    feature['id'] = feature['properties']['name']
fig = px.choropleth_mapbox(df_MO,
                           geojson=geojson,
                           color="Count",
                           locations="Area",
                           center={"lat": 1.3521, "lon": 103.8198},
                           mapbox_style="carto-positron",
                           zoom=10,
                           opacity=0.5,
                           title="Previous $1M HDBs")

fig.show()
