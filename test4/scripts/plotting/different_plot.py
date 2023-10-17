import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import json
import csv
import dash
from dash import html, dash_table, dcc, Input, Output

'''
    Description : Plot the Table, Return Table
'''
def display_table_test():
    # Read the CSV file and parse its data
    csv_file = 'scripts/algo/Excel/output/UpdatedUserHse.csv'
    df = pd.read_csv(csv_file)
    
    # Define a list of columns to remove
    columns_to_remove = ['Unnamed: 0', 'FairpricePoints', 'HosPoints', 'MallPoints', 'MRTPoints', 'ParksPoints',
                         'PriSchPoints', 'SecSchPoints', 'TertairyPoints', 'UniPoints', 'SQM_Points', 'Total_Points', 
                         'History_Avg_Point', 'Percent', 'NewPercentage', 'Coordinates', 'Link', 'Lease']  # Replace with the actual column names to remove

    # Remove the specified columns from the DataFrame
    df = df.drop(columns=columns_to_remove, errors='ignore')

    # Step 3: Create a Plotly table from the modified DataFrame
    table_fig = go.Figure(data=[go.Table(
        header=dict(values=list(df.columns)),
        cells=dict(values=[df[col] for col in df.columns]))
    ])

    # Step 4: Convert the Plotly figure to HTML
    table_html = table_fig.to_html(full_html=False)

    return table_html

def heatmap():
    geojson = json.load(open("scripts/plotting/SG_HDB_Map/SG_PlanZone_Geojson.json","r"))
    #df_H = pd.read_csv(r"C:\Users\Jongo\source\repos\SG_HDB_Map\HDB_CSV.csv")

    mapDic = {}

    #Map for current 1 Mil Houses
    df_C = pd.read_csv("scripts/algo/Excel/output/UpdatedUserHse.csv")
    for i in df_C["Location"]: #Fill dictionary with relevant data from CSV
        mapDic[i] = mapDic.get(i, 0) + 1    

    with open('scripts/plotting/SG_HDB_Map/HeatMapFrameCurrent.csv', mode='w') as csvfile: #Write that data in new CSV
        fieldnames = ["Area","Count"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in mapDic:
            writer.writerow({"Area":i, "Count":mapDic[i]})


    df_MC = pd.read_csv("scripts/plotting/SG_HDB_Map/HeatMapFrameCurrent.csv") #Open newly created CSV

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
                            title="Potential $1M HDB per area",
                            color_continuous_scale="ylorrd")

     #Step 4: Convert the Plotly figure to HTML
    table_html = fig.to_html(full_html=False)

    return table_html
