from flask import Flask, render_template
import numpy as np
import plotly.express as px
import pandas as pd


def generate_plotly_chart(map_style):

    # Replace 'data.csv' with the actual file path to your CSV file.
    file_path = "scripts/algo/Excel/output/FilteredUserHse.csv"

    # Read the CSV file into a DataFrame.
    df = pd.read_csv(file_path)

    # Split the "Coordinates" column into "Latitude" and "Longitude" columns
    df[['Latitude', 'Longitude']] = df['Coordinates'].str.split(', ', expand=True)

    # Convert the new columns to numeric data types
    df['Latitude'] = pd.to_numeric(df['Latitude'])
    df['Longitude'] = pd.to_numeric(df['Longitude'])

    # Now, your DataFrame 'df' contains two new columns: 'Latitude' and 'Longitude'.
    # You can access them like this:
    latitude_column = df['Latitude']
    longitude_column = df['Longitude']

    # Print the first few rows to verify
    print(latitude_column)

    df = px.data.carshare()

    # Define the geographical boundaries of Singapore
    min_lon = 103.59
    max_lon = 104.10
    min_lat = 1.16
    max_lat = 1.47

    # Define the number of data points you want
    num_points = 10

    # Generate random coordinates within the boundaries of Singapore
    lon_values = np.random.uniform(min_lon, max_lon, num_points)
    lat_values = np.random.uniform(min_lat, max_lat, num_points)

    # Create a DataFrame with lon and lat columns
    df = pd.DataFrame({'lon': lon_values, 'lat': lat_values})

    min = 1
    max = 100

    df['Amenties'] = 1
    df['size_dot'] = np.random.randint(min, max + 1, num_points)
    df['Description'] = "HDB House"

    fig = px.scatter_mapbox(df,
                            lon=longitude_column,
                            lat=latitude_column,
                            zoom=10,
                            color=df['Amenties'],
                            size=df['size_dot'],
                            hover_data=['Description'],
                            width=800,
                            height=600,
                            )
    fig.update_layout(mapbox_style=map_style)
    fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 10})

    # Convert Plotly chart to HTML
    plot_div = fig.to_html(full_html=False)

    return plot_div



