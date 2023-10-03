from flask import Flask, render_template
import plotly.express as px
import pandas as pd

def generate_plotly_chart():
    df = px.data.carshare()
    fig = px.scatter_mapbox(df,
                            lon=df['centroid_lon'],
                            lat=df['centroid_lat'],
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


