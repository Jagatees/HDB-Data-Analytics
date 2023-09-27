import math
import requests
import pandas as pd

def GetLongLatFromAddress(Address):
    #LocationIQ API key
    api_key = "pk.e1b6b31b46f4a037730c34a22ffdd6d3"

    Coordinates = ""

    # Construct the API request URL
    url = f"https://us1.locationiq.com/v1/search.php?key={api_key}&q={Address}&format=json"
            
    try:
        # Make the API request
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            if data:
                # Extract and append the latitude and longitude to the coordinates list
                latitude = data[0]["lat"]
                longitude = data[0]["lon"]
                Coordinates = latitude + ", " + longitude
            else:
                print(f"Location not found for address: {Address}")
        else:
            print(f"Error: Unable to access the LocationIQ API for address: {Address}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

    return Coordinates

def DistanceBetween2Coordinates(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Radius of the Earth in kilometers
    earth_radius = 6371.0

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = earth_radius * c

    return distance

def Calculate_Hse_Amenities_Dist(Hse_lat, Hse_long, Amenties_lat, Amenties_long, AmentiesName):
    distances = []

    for lat1, lon1 in zip(Hse_lat, Hse_long):
        for lat2, lon2 in zip(Amenties_lat, Amenties_long):
            distance = DistanceBetween2Coordinates(lat1, lon1, lat2, lon2)
            Coordinates = str(lat1) + ", " + str(lon1)
            distances.append({'Coordinates': Coordinates, 'Amenties_Name': AmentiesName, 'Amenties_lat': lat2, 'Amenties_lon': lon2 , 'Distance (km)': distance})

    return distances

def GetCoordinatesfromcsv(FilePath):

    column_names = ['Location_Type', 'Long', 'Lat']

    CSVLongLat = pd.read_csv(FilePath, header=None)
    CSVLongLat = CSVLongLat[[1, 6, 7]]
    CSVLongLat.columns = ['Location_Type', 'Long', 'Lat']
    CSVLongLat = CSVLongLat.drop(0)

    return CSVLongLat

def FilterDataTableByDistance(datatable, distance):
    
    filterdf = datatable[datatable['Distance (km)'] < distance]
    return filterdf


