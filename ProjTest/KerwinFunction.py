import math
import time
import requests
import pandas as pd

def GetLongLatFromAddress(AddressArray, Filepath):
    #LocationIQ API key
    api_key = "pk.02ff73880ec7a133cfe62191e54c3bd1"

    coordinatesLong = []
    coordinatesLat = []
    #Coordinates = ""

    # Iterate through the addresses and convert them to coordinates
    for address in AddressArray:
        # Construct the API request URL
        url = f"https://us1.locationiq.com/v1/search.php?key={api_key}&q={address}&format=json"
            
        try:
            # Make the API request
            with requests.Session() as session:
                response = session.get(url)

                # min 1 min no lesser
                # Add 1 min is so it give it breather time to make a request and not prevent any closing and open session at the same time 
                time.sleep(1) 
                    
                # Check if the request was successful (status code 200)
                if response.status_code == 200:
                    # Parse the JSON response
                    data = response.json()

                    if data:
                        # Extract and append the latitude and longitude to the coordinates list
                        latitude = data[0]["lat"]
                        longitude = data[0]["lon"]
                        coordinatesLong.append((longitude))
                        coordinatesLat.append((latitude))
                        #Coordinates = latitude + ", " + longitude
                    else:
                        print(f"Location not found for address: {address}")
                else:
                    print(f"Error: Unable to access the LocationIQ API for address: {address}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    AddressDataFrame = pd.read_csv(Filepath, header=None)
    AddressDataFrame.columns = ['Location_Name', 'Location_Type', 'Blk_No' ,'Address', 'Postal_Code', 'Full_Address', 'Long', 'Lat']
    AddressDataFrame = AddressDataFrame.drop(0)

    AddressDataFrame['Long'] = coordinatesLong
    AddressDataFrame['Lat'] = coordinatesLat

    AddressDataFrame.to_csv(Filepath, index=False)

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

def ReadCSVFile(FilePath):

    #Store address in this array
    AddressArray = []

    #Read CSV File
    AddressCSV = pd.read_csv(FilePath, header=None)
    AddressCSV.columns = ['Location_Name', 'Location_Type', 'Blk_No' ,'Address', 'Postal_Code', 'Full_Address', 'Long', 'Lat']
    AddressCSV = AddressCSV.drop(0)

    # Iterate through the DataFrame
    for index, row in AddressCSV.iterrows():
        # Extract values from the two columns and concatenate them

        value1 = row['Blk_No']
        value2 = row['Address']
        concatenated = str(value1) + " " + str(value2)  # Convert to string if not already

        # Append the concatenated value to the list
        AddressArray.append(concatenated)

    return AddressArray

def GetCoordinatesfromcsv(FilePath):
    CSVLongLat = pd.read_csv(FilePath, header=None)
    CSVLongLat = CSVLongLat[[0, 6, 7]]
    CSVLongLat.columns = ['Location_Name', 'Long', 'Lat']
    CSVLongLat = CSVLongLat.drop(0)

    return CSVLongLat

def GetUserDatafromcsv(FilePath):
    UserData = pd.read_csv(FilePath, header=None)
    UserData = UserData[[0, 6, 7, 8]]
    UserData.columns = ['Location_Name', 'Long', 'Lat', 'Link']
    UserData = UserData.drop(0)

    return UserData

def FilterDataTableByDistance(datatable, distance):
    
    filterdf = datatable[datatable['Distance (km)'] < distance]
    return filterdf


