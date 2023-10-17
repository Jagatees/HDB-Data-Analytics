import pandas as pd
import plotly.graph_objects as go


'''
Description: Return New Trace For Scatter Box to append to
'''
def create_scattermapbox(file_path, trace_name, colors, islegend):
    df = pd.read_csv(file_path)
    lat, lon = df['Lat'], df['Long']

    scattermapbox_trace = go.Scattermapbox(
        lat=lat,
        lon=lon,
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=10,
            color=colors,
        ),
        text='None',
        name=trace_name,
        showlegend=islegend,  # Set showlegend to control initial visibility

    )

    return scattermapbox_trace


'''
Description: Create Room Type 
'''

def room_type(room_type, title, color):

    hdb_file_path1 = "scripts/algo/Excel/output/FilteredUserHse.csv"
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
Description: format price string , return string
'''

def format_profit(profit):
    return "${:.2f}".format(profit)


'''
    Description: Plot the Map, Return Map
'''
def generate_plotly_chart(map_style, area, hdb_type):

    found_query_states = "Found Match"
    return_list = []
    center_lat = 1.3521  # Replace with your desired latitude
    center_lon = 103.8198  # Replace with your desired longitude
    zoom_level = 10  # Adjust the zoom level as needed

    # Read HDB data
    hdb_file_path1 = "scripts/algo/Excel/output/UpdatedUserHse.csv"
    df1 = pd.read_csv(hdb_file_path1)
    
    # Split coordinates into latitude and longitude columns
    df1[['Latitude', 'Longitude']] = df1['Coordinates'].str.split(
        ', ', expand=True)
    df1['Latitude'] = pd.to_numeric(df1['Latitude'])
    df1['Longitude'] = pd.to_numeric(df1['Longitude'])

    # ||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


    if area == "All" and hdb_type == "All":
         df1 = df1
    elif area != "All" and hdb_type == "All":
        df1 = df1[df1['Area'] == area]
    elif area == "All" and hdb_type != "All":
        df1 = df1[df1['Location_Type'] == hdb_type]
    elif area != "All" and hdb_type != "All":
        df1 = df1[(df1['Area'] == area) & (df1['Location_Type'] == hdb_type)]


    print(df1)
    if df1.empty:
        print("No matching data found.")
        found_query_states = 'No Match'
        
   
    text_to_display = (
        "Area: " + df1['Area'].astype(str) + "<br>" +
        "Location_Type: " + df1['Location_Type'].astype(str) + "<br>" +
        "Percetage: " + df1['NewPercentage'].astype(str) + "<br>" +
        "Profit: " + df1['Profit'].apply(format_profit).astype(str)
    )

    # Create traces for 4-room and 5-room HDB
    customQuery = go.Scattermapbox(
        lat=df1['Latitude'],
        lon=df1['Longitude'],
        mode='markers',
        marker=go.scattermapbox.Marker(
            size=20,
            color='#FF0000',
        ),
        text=text_to_display,
        name= area  + " "+ hdb_type
    )



    fairprice_file_path = "scripts/algo/Excel/Amenities/fairprice.csv"
    hospital_file_path = "scripts/algo/Excel/Amenities/HospitalClinic.csv"
    malls_file_path = 'scripts/algo/Excel/Amenities/Malls.csv'
    mrt_file_path = 'scripts/algo/Excel/Amenities/MRTData.csv'
    park_file_path = 'scripts/algo/Excel/Amenities/Parks.csv'
    pri_file_path = 'scripts/algo/Excel/Amenities/primaryschool.csv'
    secon_file_path = 'scripts/algo/Excel/Amenities/secondaryschool.csv'
    ter_file_path = 'scripts/algo/Excel/Amenities/tertiaryschool.csv'
    uni_file_path = 'scripts/algo/Excel/Amenities/univeristies.csv'

    # Create a figure with all the traces
    fig = go.Figure(data=[
        customQuery,
        create_scattermapbox(fairprice_file_path, 'FairPrice', "#0000FF", True),
        create_scattermapbox(hospital_file_path, 'Hospital', "#FFFF00", True),
        create_scattermapbox(malls_file_path, 'Malls', "#FFEBCD", True),
        create_scattermapbox(mrt_file_path, 'MRT', "#FFA500", True),
        create_scattermapbox(park_file_path, 'Parks', "#90EE90", True),
        create_scattermapbox(pri_file_path, 'Primary', "#CBC3E3", True),
        create_scattermapbox(secon_file_path, 'Secondary', "#FFB6C1", True),
        create_scattermapbox(ter_file_path, 'Tertiary', "#C4A484", True),
        create_scattermapbox(uni_file_path, 'Univeristies', "#FFD700", True),
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

    return_list.append(plot_div)
    return_list.append(found_query_states)

    return return_list


