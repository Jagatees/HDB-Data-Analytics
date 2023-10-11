import plotly.graph_objects as go
import pandas as pd

def plot_simple_map():
    # Read the CSV file
    df = pd.read_csv('ProjTest\Excel Data\FilteredUserHse.csv')

    # Split coordinates into latitude and longitude columns
    df[['Latitude', 'Longitude']] = df['Coordinates'].str.split(', ', expand=True)

    text_to_display = (
        "Area: " + df['Area'].astype(str) + "<br>" +
        "Location_Type: " + df['Location_Type'].astype(str)
    )

    # Create a scattermapbox trace
    trace = go.Scattermapbox(
        lat=df['Latitude'],
        lon=df['Longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=15,
            color='#FFFF00',
        ),
        text=text_to_display
    )

    # Create the figure
    fig = go.Figure(data=[trace])

    center_lat = 1.3521  # Replace with your desired latitude
    center_lon = 103.8198  # Replace with your desired longitude
    zoom_level = 10  # Adjust the zoom level as needed

    # Update the layout of the map
    fig.update_layout(
        mapbox_style="open-street-map",
        mapbox_center={"lat": center_lat, "lon": center_lon},
        mapbox_zoom=zoom_level,
        height=720,
        width=980,
        title_text="Simple Map",
        title_x=0.5
    )
    fig.show()
    input("Press Enter to exit...")

plot_simple_map()