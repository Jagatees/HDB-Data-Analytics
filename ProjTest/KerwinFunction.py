import math
import time
import requests
import pandas as pd
from sklearn.linear_model import LinearRegression
from statistics import mean
import numpy as np
from sklearn.metrics import r2_score

lease_points = {
    89: 0.05,
    79: 0.04,
    69: 0.035,
    59: 0.03,
    49: 0.025,
    39: 0.02,
    29: 0.015,
    19: 0.01,
}

sqm_points = {
    149: 0.05,
    109: 0.04,
    90: 0.035,
    70: 0.025,
    45: 0.02,
}

def calculate_lease_points(remaining_lease_str):
    remaining_lease = int(remaining_lease_str)
    for years, points in lease_points.items():
        if remaining_lease >= years:
            return points
    return 0.005

def calculate_sqm_points(floor_area_sqm):
    for sqm, points in sqm_points.items():
        if float(floor_area_sqm) >= sqm:  # Convert floor_area_sqm to float
            return points
    return 1 

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

                        CheckLong = float(latitude)
                        CheckLat = float(longitude)

                        if CheckLong > 0 and CheckLat > 0:
                            coordinatesLong.append((longitude))
                            coordinatesLat.append((latitude))
                        else:
                            coordinatesLong.append((0))
                            coordinatesLat.append((0))
                        #Coordinates = latitude + ", " + longitude
                    else:
                        print(f"Location not found for address: {address}")
                else:
                    print(f"Error: Unable to access the LocationIQ API for address: {address}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    AddressDataFrame = pd.read_csv(Filepath, header=None)
    AddressDataFrame.columns = ['Location_Name', 'Location_Type', 'Blk_No' ,'Address', 'Postal_Code', 'Full_Address', 'Long', 'Lat', 
                                'floor_area_sqm', 'remaining_lease', 'Price', 'Link', 'Leased_Used', 'Num_Bed', 'Num_Toilet']
    AddressDataFrame = AddressDataFrame.drop(0)
    
    AddressDataFrame['Long'] = coordinatesLong
    AddressDataFrame['Lat'] = coordinatesLat

    for index, row in AddressDataFrame.iterrows():
        if row['Long'] == 0:
            AddressDataFrame.drop(index, inplace=True)

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
    AddressCSV = AddressCSV[[0, 1, 2, 3, 6, 7]]
    AddressCSV.columns = ['Location_Name', 'Location_Type', 'Blk_No' ,'Address', 'Long', 'Lat']
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
    CSVLongLat = CSVLongLat[[0, 1, 6, 7]]
    CSVLongLat.columns = ['Location_Name','Location_Type', 'Long', 'Lat']
    CSVLongLat = CSVLongLat.drop(0)

    return CSVLongLat

def GetHistoryfromcsv(FilePath):
    CSVLongLat = pd.read_csv(FilePath, header=None)
    CSVLongLat = CSVLongLat[[1, 2, 7, 8, 10, 11]]
    CSVLongLat.columns = ['Location_Name','Location_Type', 'Long', 'Lat', 'remaining_lease', 'floor_area_sqm']
    CSVLongLat = CSVLongLat.drop(0)

    return CSVLongLat

def GetUserDatafromcsv(FilePath):
    UserData = pd.read_csv(FilePath, header=None)
    UserData = UserData[[0, 1, 6, 7, 8, 9, 11]]
    UserData.columns = ['Location_Name','Location_Type' , 'Long', 'Lat', 'remaining_lease', 'floor_area_sqm', 'Link']
    UserData = UserData.drop(0)

    return UserData

def FilterDataTableByDistance(datatable, distance):
    
    filterdf = datatable[datatable['Distance (km)'] < distance]
    return filterdf

def Preediction(Dataframe, year):
    Predict_DF = Dataframe.copy()

    # Specify the flat types to predict
    flat_types_to_predict = ["2 ROOM", "3 ROOM", "4 ROOM", "5 ROOM", "EXECUTIVE"]

    # Create a DataFrame to store the prediction results
    prediction_results = []

    # Loop through towns
    for town in ["ANG MO KIO", "BEDOK", "BISHAN", "BUKIT BATOK", "BUKIT MERAH", "BUKIT PANJANG", "BUKIT TIMAH"
                , "CENTRAL AREA", "CHOA CHU KANG", "CLEMENTI", "GEYLANG", "HOUGANG", "JURONG EAST", "JURONG WEST"
                , "KALLANG/WHAMPOA", "MARINE PARADE", "PASIR RIS", "PUNGGOL", "QUEENSTOWN", "SEMBAWANG", "SENGKANG"
                , "SERANGOON", "TAMPINES", "TOA PAYOH", "WOODLANDS", "YISHUN"]:
        for flat_type in flat_types_to_predict:

            # Filter data for the specified town and flat type
            filtered_data = Predict_DF[(Predict_DF['Town'] == town) & (Predict_DF['Flat_Type'] == flat_type)]

            if not filtered_data.empty:
                # Separate the features (X) and target (y)
                X = filtered_data[['Year']]
                y = filtered_data['Price']

                # Create a linear regression model
                model = LinearRegression()

                # Fit the model to the data
                model.fit(X, y)

                # Predict price
                predicted_price = model.predict([[year]])[0]

                # Append the prediction results to the list
                prediction_results.append({"Year": year,"Town": town,"Flat_Type": flat_type,"Predicted_Price": predicted_price})
            else:
                # If data is not available, set the price to 0
                prediction_results.append({"Year": year,"Town": town,"Flat_Type": flat_type,"Predicted_Price": 0})

    # Create a DataFrame from the prediction results
    prediction_df = pd.DataFrame(prediction_results)

    # Display the prediction results
    print(prediction_df)
