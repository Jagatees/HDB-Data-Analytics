from flask import Flask, render_template
import numpy as np
import plotly.express as px
import pandas as pd

def generate_plotly_chart():
    df = px.data.carshare()

    # Define the geographical boundaries of Singapore
    min_lon = 103.59
    max_lon = 104.10
    min_lat = 1.16
    max_lat = 1.47

    # Define the number of data points you want
    num_points = 100

    # Generate random coordinates within the boundaries of Singapore
    lon_values = np.random.uniform(min_lon, max_lon, num_points)
    lat_values = np.random.uniform(min_lat, max_lat, num_points)

    # Create a DataFrame with lon and lat columns
    df = pd.DataFrame({'lon': lon_values, 'lat': lat_values})

    # Generate random values for color and size columns
    min_color = 1
    max_color = 10
    min_size = 1
    max_size = 100

    df['peak_hour'] = np.random.randint(min_color, max_color + 1, num_points)
    df['car_hours'] = np.random.randint(min_size, max_size + 1, num_points)




    fig = px.scatter_mapbox(df,
                            lon=df['lon'],
                            lat=df['lat'],
                            zoom=10,
                            color=df['peak_hour'],
                            size=df['car_hours'],
                            width=1200,
                            height=900,
                            title='Car Share Scatter Map',
                            )
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r": 0, "t": 50, "l": 0, "b": 10})

    # Convert Plotly chart to HTML
    plot_div = fig.to_html(full_html=False)

    return plot_div


