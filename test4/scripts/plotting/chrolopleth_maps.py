import pandas as pd
import plotly.graph_objects as go


'''
    Description : Return New Trace For Scatter Box to append to
'''
def create_scattermapbox(file_path, trace_name):
    df = pd.read_csv(file_path)
    lat, lon = df['Lat'], df['Long']

    scattermapbox_trace = go.Scattermapbox(
        lat=lat,
        lon=lon,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=5,
            color="#00ff00",
        ),
        text='None',  
        name=trace_name,
    )

    return scattermapbox_trace


'''
    Description : Plot the Map, Return Map
'''
def generate_plotly_chart(map_style):

    center_lat = 1.3521  # Replace with your desired latitude
    center_lon = 103.8198  # Replace with your desired longitude
    zoom_level = 10  # Adjust the zoom level as needed

    # for hdb is a special
    hdb_file_path1 = "scripts/algo/Excel/output/FilteredUserHse.csv"
    df1 = pd.read_csv(hdb_file_path1)
    df1[['Latitude', 'Longitude']] = df1['Coordinates'].str.split(
        ', ', expand=True)
    df1['Latitude'] = pd.to_numeric(df1['Latitude'])
    df1['Longitude'] = pd.to_numeric(df1['Longitude'])

    # DF1
    hdb_house_onsale = go.Scattermapbox(
        lat=df1['Latitude'],
        lon=df1['Longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=15,
            color="#ff0000",
        ),
        text= df1['Total_Points'],  # If df1 has "Total_Points"
        name="HDB House",
    )

    # Replace with the path to your second CSV file
    fairprice_file_path = "scripts/algo/Excel/Amenities/fairprice.csv"
    hospital_file_path = "scripts/algo/Excel/Amenities/HospitalClinic.csv"

    # Create a figure with both traces
    fig = go.Figure(data=[
        hdb_house_onsale, 
        create_scattermapbox(fairprice_file_path, 'FairPrice'), 
        create_scattermapbox(hospital_file_path, 'Hospital')])

    fig.update_layout(mapbox_style=map_style, 
                      mapbox_center={"lat": center_lat, "lon": center_lon}, 
                      mapbox_zoom=zoom_level,
                      height=720,
                      width=980,
                      title_text = "TITLE",
                      title_x = 0.5,
                      )
    plot_div = fig.to_html(full_html=False)

    return plot_div
