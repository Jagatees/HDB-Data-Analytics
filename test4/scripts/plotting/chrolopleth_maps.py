import pandas as pd
import plotly.graph_objects as go


'''
Description: Return New Trace For Scatter Box to append to
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
Description: Create Room Type 
'''

def room_type(room_type, title, color):

    hdb_file_path1 = "scripts/algo/Excel/percentage/UpdatedUserHse.csv"
    df1 = pd.read_csv(hdb_file_path1)
    
    # Split coordinates into latitude and longitude columns
    df1[['Latitude', 'Longitude']] = df1['Coordinates'].str.split(
        ', ', expand=True)
    df1['Latitude'] = pd.to_numeric(df1['Latitude'])
    df1['Longitude'] = pd.to_numeric(df1['Longitude'])

    # FILTER LOCATION TYPE
    df1 = df1[df1['Location_Type'] == room_type]

    text_to_display = (
        "Final Percentage: " + df1['Final_Percentage'].astype(str) + "<br>" +
        "Area: " + df1['Area'].astype(str) + "<br>" +
        "Location_Type: " + df1['Location_Type'].astype(str)
    )

    # Create traces for 4-room and 5-room HDB
    hdb_house_onsale = go.Scattermapbox(
        lat=df1['Latitude'],
        lon=df1['Longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=15,
            color=color,
        ),
        text=text_to_display,
        name=title,
    )

    return hdb_house_onsale



'''
Description: Plot the Map, Return Map
'''

def generate_plotly_chart(map_style, area, hdb_type):
    center_lat = 1.3521  # Replace with your desired latitude
    center_lon = 103.8198  # Replace with your desired longitude
    zoom_level = 10  # Adjust the zoom level as needed

    # Read HDB data
    hdb_file_path1 = "scripts/algo/Excel/percentage/UpdatedUserHse.csv"
    df1 = pd.read_csv(hdb_file_path1)
    
    # Split coordinates into latitude and longitude columns
    df1[['Latitude', 'Longitude']] = df1['Coordinates'].str.split(
        ', ', expand=True)
    df1['Latitude'] = pd.to_numeric(df1['Latitude'])
    df1['Longitude'] = pd.to_numeric(df1['Longitude'])

    # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    area_text = ""
    hdb_type_text = ""
    
    if area != "All" and hdb_type != "All":
        df1 = df1[(df1['Area'] == area) & (df1['Location_Type'] == hdb_type)]
        area_text = "All Area"
        hdb_type_text = "& type"
    elif area != "All" and hdb_type == "All":
        df1 = df1[df1['Area'] == area]
        area_text = area
        hdb_type_text = "All type"
    elif area == "All" and hdb_type != "All":
        df1 = df1[df1['Location_Type'] == hdb_type]
        area_text = "ALL Area"
        hdb_type_text = hdb_type




    text_to_display = (
        "Final Percentage: " + df1['Final_Percentage'].astype(str) + "<br>" +
        "Area: " + df1['Area'].astype(str) + "<br>" +
        "Location_Type: " + df1['Location_Type'].astype(str)
    )

    # Create traces for 4-room and 5-room HDB
    customQuery = go.Scattermapbox(
        lat=df1['Latitude'],
        lon=df1['Longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=15,
            color='#FFFF00',
        ),
        text=text_to_display,
        name= area_text  + " "+ hdb_type_text
    )



    fairprice_file_path = "scripts/algo/Excel/Amenities/fairprice.csv"
    hospital_file_path = "scripts/algo/Excel/Amenities/HospitalClinic.csv"

    # Create a figure with all the traces
    fig = go.Figure(data=[
        customQuery,
        create_scattermapbox(fairprice_file_path, 'FairPrice'),
        create_scattermapbox(hospital_file_path, 'Hospital')
    ])


    # Update the layout of the map
    fig.update_layout(
        mapbox_style=map_style,
        mapbox_center={"lat": center_lat, "lon": center_lon},
        mapbox_zoom=zoom_level,
        height=720,
        width=980, 
        title_text="Map HDB on Sale",
        title_x=0.5,

        legend=dict(
            title="Legends",  
            bgcolor="rgba(255, 255, 255, 0.6)", 
            bordercolor="black",    
            borderwidth=1,          
            font=dict(size=12),     
        )
    )
    
    plot_div = fig.to_html(full_html=False)

    return plot_div


