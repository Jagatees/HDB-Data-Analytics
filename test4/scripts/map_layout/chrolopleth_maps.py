import random
from flask import Flask, render_template
import numpy as np
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go




def generate_plotly_chart(map_style):
   
    file_path1 = "scripts/algo/Excel/output/FilteredUserHse.csv"
    file_path2 = "scripts/algo/Excel/Amenities/fairprice.csv"  # Replace with the path to your second CSV file

    df1 = pd.read_csv(file_path1)
    df2 = pd.read_csv(file_path2)

    # Split and convert coordinates for the first DataFrame (if needed)
    df1[['Latitude', 'Longitude']] = df1['Coordinates'].str.split(', ', expand=True)
    df1['Latitude'] = pd.to_numeric(df1['Latitude'])
    df1['Longitude'] = pd.to_numeric(df1['Longitude'])

    # Extract latitude and longitude columns for the second DataFrame
    lat2 = df2['Lat']
    lon2 = df2['Long']

    # Combine latitude and longitude columns from both DataFrames
    latitude_column = pd.concat([df1['Latitude'], lat2])
    longitude_column = pd.concat([df1['Longitude'], lon2])
    
    # Define different colors for df1 and df2
    color1 = "#ff0000"  # Red for df1
    color2 = "#00ff00"  # Green for df2

    # Create a trace for df1
    trace1 = go.Scattermapbox(
        lat=df1['Latitude'],
        lon=df1['Longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=20,
            color=color1,
        ),
        text=df1['Total_Points'],  # If df1 has "Total_Points"
    )

    # Create a trace for df2
    trace2 = go.Scattermapbox(
        lat=lat2,
        lon=lon2,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=20,
            color=color2,
        ),
        text=None,  # No "Total_Points" in df2
    )

    # Set the desired center coordinates and zoom level
    center_lat = 1.3521  # Replace with your desired latitude
    center_lon = 103.8198  # Replace with your desired longitude
    zoom_level = 10  # Adjust the zoom level as needed

    # Create a figure with both traces
    fig = go.Figure(data=[trace1, trace2])

    fig.update_layout(mapbox_style=map_style, mapbox_center={"lat": center_lat, "lon": center_lon}, mapbox_zoom=zoom_level)
    plot_div = fig.to_html(full_html=False) 
    

    return plot_div


# def generate_plotly_chart(map_style):

#     # Data set 2
#     new_df = pd.read_csv("scripts/algo/Excel/Amenities/fairprice.csv")
#     new_lat = new_df['Lat']
#     new_long = new_df['Long']
    

#     # Replace 'data.csv' with the actual file path to your CSV file.
#     file_path = "scripts/algo/Excel/output/FilteredUserHse.csv"

#     # Read the CSV file into a DataFrame.
#     df = pd.read_csv(file_path)
#     print("Length of dataset : " + str(len(df)) + " " + file_path )

#     # Split the "Coordinates" column into "Latitude" and "Longitude" columns
#     df[['Latitude', 'Longitude']] = df['Coordinates'].str.split(', ', expand=True)

#     # Convert the new columns to numeric data types
#     df['Latitude'] = pd.to_numeric(df['Latitude'])
#     df['Longitude'] = pd.to_numeric(df['Longitude'])

#     # Now, your DataFrame 'df' contains two new columns: 'Latitude' and 'Longitude'.
#     # You can access them like this:
#     latitude_column = df['Latitude']
#     longitude_column = df['Longitude']

#     num_points = len(df)
  
#     df['Amenties'] = np.random.randint(1, 100, num_points)
#     df['size_dot'] = 1
#     df['Description'] = "Plot1"

   
#     # work on the size problem 
#     # able to disable the data set and plot the map

#     # House 
#     fig = px.scatter_mapbox(df,
#                             lon=longitude_column,
#                             lat=latitude_column,
#                             zoom=10,
#                             color_discrete_sequence=['red'],
#                             # size=df['size_dot'],
#                             size_max = 100,
#                             hover_data=['Description'],
#                             width=800,
#                             height=600,
#                             opacity= 1
#                             )
    


#     # num_points_new_df = len(new_df)

#     # new_df['Amenties_2'] = np.random.randint(1, 100, num_points_new_df)
#     # fixed_marker_size = 1  # Adjust the size value as needed

#     # new_df['size_dot_2'] = fixed_marker_size
#     # new_df['Description_2'] = "FairPrice"
    

#     # # Fairprice
#     # fig.add_trace(px.scatter_mapbox(new_df,
#     #                             lon=new_long,
#     #                             lat=new_lat,
#     #                             zoom=10,  # Adjust the zoom level as needed
#     #                             color_discrete_sequence=['blue'],  # Specify the color column for the new data
#     #                             size=new_df['size_dot_2'],  # Specify the size column for the new data
#     #                             hover_data=['Description_2'],  # Specify hover data for the new data
#     #                             width=800,
#     #                             height=600,
#     #                             opacity= 1
#     #                             ).data[0]  # Extract the data from the new scatter plot
#     #          )
#     fig.update_layout(mapbox_style=map_style)
#     fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 10})



#     # Convert Plotly chart to HTML
#     plot_div = fig.to_html(full_html=False)

#     return plot_div