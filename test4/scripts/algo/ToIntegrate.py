import math
import time
import requests
from sklearn.linear_model import LinearRegression
from statistics import mean
import numpy as np
from sklearn.metrics import r2_score
from statistics import mean
import pandas as pd
import csv



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
    AddressDataFrame.columns = ['Location_Name', 'Location_Type', 'Blk_No' ,'Address', 'Postal_Code', 'Full_Address', 'Long', 'Lat']
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
    CSVLongLat = CSVLongLat[[0, 1, 6, 7]]
    CSVLongLat.columns = ['Location_Name','Location_Type', 'Long', 'Lat']
    CSVLongLat = CSVLongLat.drop(0)

    return CSVLongLat

def GetUserDatafromcsv(FilePath):
    UserData = pd.read_csv(FilePath, header=None)
    UserData = UserData[[0, 1, 6, 7, 8]]
    UserData.columns = ['Location_Name','Location_Type' , 'Long', 'Lat', 'Link']
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

'''
    Predicition & Algo
'''


def predicition_for_percentage():
    csv_file = 'scripts/algo/Excel/output/HistoryResaleData.csv'
    HistoryResaleDataDF = pd.read_csv(csv_file, header=None)

    #Take only selected col
    HistoryResaleDataDF = HistoryResaleDataDF[[0, 1, 2, 10]]
    #Change col name
    HistoryResaleDataDF.columns = ['Year', 'Town', 'Flat_Type' ,'Price']
    #Drop first row
    HistoryResaleDataDF = HistoryResaleDataDF.drop(0)

    # Convert the "Price" column to numeric
    HistoryResaleDataDF['Price'] = pd.to_numeric(HistoryResaleDataDF['Price'])
    HistoryResaleDataDF['Year'] = pd.to_numeric(HistoryResaleDataDF['Year'])

    #get all the unique values and find the average price of it.
    UniqueGroupValues = HistoryResaleDataDF.groupby(['Year', 'Town', 'Flat_Type'])['Price'].mean().reset_index()
    UniqueGroupValues_sorted = UniqueGroupValues.sort_values(by=['Year', 'Town'])

    print('Filter Done')
    #Save dataframe into new csv file
    UniqueGroupValues_sorted.to_csv('scripts/algo/Excel/output/Cleaned_UnPredicted_HistoryData.csv', index=False)

    Actual2023DF = UniqueGroupValues_sorted[UniqueGroupValues_sorted['Year'] == 2023]

    Predict2023_DF = UniqueGroupValues_sorted.copy()

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
            filtered_data = Predict2023_DF[(Predict2023_DF['Town'] == town) & (Predict2023_DF['Flat_Type'] == flat_type)]

            if not filtered_data.empty:
                # Separate the features (X) and target (y)
                X = filtered_data[['Year']]
                y = filtered_data['Price']

                # Create a linear regression model
                model = LinearRegression()

                # Fit the model to the data
                model.fit(X, y)

                # Predict price
                predicted_price = model.predict([[2023]])[0]

                # Append the prediction results to the list
                prediction_results.append({"Year": 2023,"Town": town,"Flat_Type": flat_type,"Predicted_Price": predicted_price})
            else:
                # If data is not available, set the price to 0
                prediction_results.append({"Year": 2023,"Town": town,"Flat_Type": flat_type,"Predicted_Price": 0})

    # Create a DataFrame from the prediction results
    prediction_2023_df = pd.DataFrame(prediction_results)
    print(prediction_2023_df)

    merged_Predictiondf = Actual2023DF.merge(prediction_2023_df[['Year', 'Town', 'Flat_Type', 'Predicted_Price']], on=['Year', 'Town', 'Flat_Type'], how='left')

    # Loop through the PredictedPrice column and replace empty values with 0
    for index, row in merged_Predictiondf.iterrows():
        if pd.isna(row['Predicted_Price']):
            merged_Predictiondf.at[index, 'Predicted_Price'] = 0

    merged_Predictiondf["Accuracy_Percentage"] = merged_Predictiondf["Predicted_Price"] / merged_Predictiondf["Price"] * 100

    Accuracy = merged_Predictiondf["Accuracy_Percentage"].mean()
    Accuracy_percentage = math.floor(Accuracy)

    merged_Predictiondf.to_csv('scripts/algo/Excel/output/Cleaned_HistoryData.csv', index=False)

    print(str(Accuracy_percentage) + "%")

def algo():
    #CSV File Paths
    FairpriceFilePath = 'scripts/algo/Excel/Amenities/fairprice.csv'
    HospitalFilePath = 'scripts/algo/Excel/Amenities/HospitalClinic.csv'
    MallsFilePath = 'scripts/algo/Excel/Amenities/Malls.csv'
    MRTDataFilePath = 'scripts/algo/Excel/Amenities/MRTData.csv'
    ParksFilePath = 'scripts/algo/Excel/Amenities/Parks.csv'
    PriSchFilePath = 'scripts/algo/Excel/Amenities/primaryschool.csv'
    SecSchFilePath = 'scripts/algo/Excel/Amenities/secondaryschool.csv'
    TertiaryFilePath = 'scripts/algo/Excel/Amenities/tertiaryschool.csv'
    UniversityFilePath = 'scripts/algo/Excel/Amenities/univeristies.csv'
    MDollarHseFilePath = 'scripts/algo/Excel/output/MillionDollarHse.csv'

    #Add scrapping code here
    UserHseFilePath = 'scripts/algo/Excel/output/DummyUserAddress.csv'

    #Amenties Points
    Hospital_ClinicPoint = 5
    SchoolsPoint = 4
    MRTPoint = 3
    Supermarket_MallPoint = 2
    ParksPoint = 1


    FairpriceDT = GetCoordinatesfromcsv(FairpriceFilePath)
    HospitalDT = GetCoordinatesfromcsv(HospitalFilePath)
    MallsDT = GetCoordinatesfromcsv(MallsFilePath)
    MRTDataDT = GetCoordinatesfromcsv(MRTDataFilePath)
    ParksDT = GetCoordinatesfromcsv(ParksFilePath)
    PriSchDT = GetCoordinatesfromcsv(PriSchFilePath)
    SecSchDT = GetCoordinatesfromcsv(SecSchFilePath)
    TertairyDT = GetCoordinatesfromcsv(TertiaryFilePath)
    UniversityDT = GetCoordinatesfromcsv(UniversityFilePath)
    MDollarHseDT =  GetCoordinatesfromcsv(MDollarHseFilePath)
    UserHseDT = GetUserDatafromcsv(UserHseFilePath)

    #Remove all the duplicated values
    MDollarHseDF = MDollarHseDT.drop_duplicates() 
    UserHseDF = UserHseDT.drop_duplicates()


    #Retrieve the long and lat and store them indivually into a list
    FairpriceLong = FairpriceDT['Long'].tolist()
    FairpriceLat = FairpriceDT['Lat'].tolist()
    HospitalLong = HospitalDT['Long'].tolist()
    HospitalLat = HospitalDT['Lat'].tolist()
    MallsLong = MallsDT['Long'].tolist()
    MallsLat = MallsDT['Lat'].tolist()
    MRTLong = MRTDataDT['Long'].tolist()
    MRTLat = MRTDataDT['Lat'].tolist()
    ParksLong = ParksDT['Long'].tolist()
    ParksLat = ParksDT['Lat'].tolist()
    PriSchLong = PriSchDT['Long'].tolist()
    PriSchLat = PriSchDT['Lat'].tolist()
    SecSchLong = SecSchDT['Long'].tolist()
    SecSchLat = SecSchDT['Lat'].tolist()
    TertairyLong = TertairyDT['Long'].tolist()
    TertairyLat = TertairyDT['Lat'].tolist()
    UniLong = UniversityDT['Long'].tolist()
    UniLat = UniversityDT['Lat'].tolist()
    MDollarHseLong = MDollarHseDF['Long'].tolist()
    MDollarHseLat = MDollarHseDF['Lat'].tolist()
    UserHseLong = UserHseDF['Long'].tolist()
    UserHseLat = UserHseDF['Lat'].tolist()

    #Convert string list to float list
    FairpriceLat_Float = [eval(x) for x in FairpriceLat]
    FairpriceLong_Float = [eval(x) for x in FairpriceLong]
    HospitalLat_Float = [eval(x) for x in HospitalLat]
    HospitalLong_Float = [eval(x) for x in HospitalLong]
    MallsLat_Float = [eval(x) for x in MallsLat]
    MallsLong_Float = [eval(x) for x in MallsLong]
    MRTLat_Float = [eval(x) for x in MRTLat]
    MRTLong_Float = [eval(x) for x in MRTLong]
    ParksLat_Float = [eval(x) for x in ParksLat]
    ParksLong_Float = [eval(x) for x in ParksLong]
    PriSchLat_Float = [eval(x) for x in PriSchLat]
    PriSchLong_Float = [eval(x) for x in PriSchLong]
    SecSchLat_Float = [eval(x) for x in SecSchLat]
    SecSchLong_Float = [eval(x) for x in SecSchLong]
    TertairyLat_Float = [eval(x) for x in TertairyLat]
    TertairyLong_Float = [eval(x) for x in TertairyLong]
    UniLat_Float = [eval(x) for x in UniLat]
    UniLong_Float = [eval(x) for x in UniLong]
    MDollarHseLat_Float = [eval(x) for x in MDollarHseLat]
    MDollarHseLong_Float = [eval(x) for x in MDollarHseLong]
    UserHseLat_Float = [eval(x) for x in UserHseLat]
    UserHseLong_Float = [eval(x) for x in UserHseLong]

    #Calculate distance between MDollarhse and the amenties
    MDollarHse_FairpriceDist = Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, FairpriceLat_Float, FairpriceLong_Float, 'Fairprice')
    MDollarHse_FairpriceDT = pd.DataFrame(MDollarHse_FairpriceDist)

    MDollarHse_HosDist = Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, HospitalLat_Float, HospitalLong_Float, 'HosClinic')
    MDollarHse_HosDT = pd.DataFrame(MDollarHse_HosDist)

    MDollarHse_MallsDist = Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, MallsLat_Float, MallsLong_Float, 'Malls')
    MDollarHse_MallsDT = pd.DataFrame(MDollarHse_MallsDist)

    MDollarHse_MRTDist = Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, MRTLat_Float, MRTLong_Float, 'MRT')
    MDollarHse_MRTDT = pd.DataFrame(MDollarHse_MRTDist)

    MDollarHse_ParksDist = Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, ParksLat_Float, ParksLong_Float, 'Parks')
    MDollarHse_ParksDT = pd.DataFrame(MDollarHse_ParksDist)

    MDollarHse_PriSchDist = Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, PriSchLat_Float, PriSchLong_Float, 'Primary School')
    MDollarHse_PriSchDT = pd.DataFrame(MDollarHse_PriSchDist)

    MDollarHse_SecSchDist = Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, SecSchLat_Float, SecSchLong_Float, 'Secondary School')
    MDollarHse_SecSchDT = pd.DataFrame(MDollarHse_SecSchDist)

    MDollarHse_TertairyDist = Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, TertairyLat_Float, TertairyLong_Float, 'Tertairy')
    MDollarHse_TertairyDT = pd.DataFrame(MDollarHse_TertairyDist)

    MDollarHse_UniDist = Calculate_Hse_Amenities_Dist(MDollarHseLat_Float, MDollarHseLong_Float, UniLat_Float, UniLong_Float, 'Uni')
    MDollarHse_UniDT = pd.DataFrame(MDollarHse_UniDist)

    #Calculate distance between Userhse and the amenties

    UserHse_FairpriceDist = Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, FairpriceLat_Float, FairpriceLong_Float, 'Fairprice')
    UserHse_FairpriceDT = pd.DataFrame(UserHse_FairpriceDist)


    UserHse_HosDist = Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, HospitalLat_Float, HospitalLong_Float, 'HosClinic')
    UserHse_HosDT = pd.DataFrame(UserHse_HosDist)


    UserHse_MallsDist = Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, MallsLat_Float, MallsLong_Float, 'Malls')
    UserHse_MallsDT = pd.DataFrame(UserHse_MallsDist)


    UserHse_MRTDist = Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, MRTLat_Float, MRTLong_Float, 'MRT')
    UserHse_MRTDT = pd.DataFrame(UserHse_MRTDist)


    UserHse_ParksDist = Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, ParksLat_Float, ParksLong_Float, 'Parks')
    UserHse_ParksDT = pd.DataFrame(UserHse_ParksDist)


    UserHse_PriSchDist = Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, PriSchLat_Float, PriSchLong_Float, 'Primary School')
    UserHse_PriSchDT = pd.DataFrame(UserHse_PriSchDist)


    UserHse_SecSchDist = Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, SecSchLat_Float, SecSchLong_Float, 'Secondary School')
    UserHse_SecSchDT = pd.DataFrame(UserHse_SecSchDist)


    UserHse_TertairyDist = Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, TertairyLat_Float, TertairyLong_Float, 'Tertairy')
    UserHse_TertairyDT = pd.DataFrame(UserHse_TertairyDist)


    UserHse_UniDist = Calculate_Hse_Amenities_Dist(UserHseLat_Float, UserHseLong_Float, UniLat_Float, UniLong_Float, 'Uni')
    UserHse_UniDT = pd.DataFrame(UserHse_UniDist)


    #Filter and get all amenties within 1km radius
    DistanceinKM = 1

    FilterMDollarHse_FairpriceDT = FilterDataTableByDistance(MDollarHse_FairpriceDT, DistanceinKM)
    FilterMDollarHse_HosDT = FilterDataTableByDistance(MDollarHse_HosDT, DistanceinKM)
    FilterMDollarHse_MallsDT = FilterDataTableByDistance(MDollarHse_MallsDT, DistanceinKM)
    FilterMDollarHse_MRTDT = FilterDataTableByDistance(MDollarHse_MRTDT, DistanceinKM)
    FilterMDollarHse_ParksDT = FilterDataTableByDistance(MDollarHse_ParksDT, DistanceinKM)
    FilterMDollarHse_PriSchDT = FilterDataTableByDistance(MDollarHse_PriSchDT, DistanceinKM)
    FilterMDollarHse_SecSchDT = FilterDataTableByDistance(MDollarHse_SecSchDT, DistanceinKM)
    FilterMDollarHse_TertairyDT = FilterDataTableByDistance(MDollarHse_TertairyDT, DistanceinKM)
    FIlterMDollarHse_UniDT = FilterDataTableByDistance(MDollarHse_UniDT, DistanceinKM)

    FilterUserHse_FairpriceDT = FilterDataTableByDistance(UserHse_FairpriceDT, DistanceinKM)
    FilterUserHse_HosDT = FilterDataTableByDistance(UserHse_HosDT, DistanceinKM)
    FilterUserHse_MallsDT = FilterDataTableByDistance(UserHse_MallsDT, DistanceinKM)
    FilterUserHse_MRTDT = FilterDataTableByDistance(UserHse_MRTDT, DistanceinKM)
    FilterUserHse_ParksDT = FilterDataTableByDistance(UserHse_ParksDT, DistanceinKM)
    FilterUserHse_PriSchDT = FilterDataTableByDistance(UserHse_PriSchDT, DistanceinKM)
    FilterUserHse_SecSchDT = FilterDataTableByDistance(UserHse_SecSchDT, DistanceinKM)
    FilterUserHse_TertairyDT = FilterDataTableByDistance(UserHse_TertairyDT, DistanceinKM)
    FIlterUserHse_UniDT = FilterDataTableByDistance(UserHse_UniDT, DistanceinKM)

    #Convert KM to Meters
    FilterMDollarHse_FairpriceDT['Distance(M)'] = FilterMDollarHse_FairpriceDT['Distance (km)'] * 1000
    FilterMDollarHse_HosDT['Distance(M)'] = FilterMDollarHse_HosDT['Distance (km)'] * 1000
    FilterMDollarHse_MallsDT['Distance(M)'] = FilterMDollarHse_MallsDT['Distance (km)'] * 1000
    FilterMDollarHse_MRTDT['Distance(M)'] = FilterMDollarHse_MRTDT['Distance (km)'] * 1000
    FilterMDollarHse_ParksDT['Distance(M)'] = FilterMDollarHse_ParksDT['Distance (km)'] * 1000
    FilterMDollarHse_PriSchDT['Distance(M)'] = FilterMDollarHse_PriSchDT['Distance (km)'] * 1000
    FilterMDollarHse_SecSchDT['Distance(M)'] = FilterMDollarHse_SecSchDT['Distance (km)'] * 1000
    FilterMDollarHse_TertairyDT['Distance(M)'] = FilterMDollarHse_TertairyDT['Distance (km)'] * 1000
    FIlterMDollarHse_UniDT['Distance(M)'] = FIlterMDollarHse_UniDT['Distance (km)'] * 1000

    FilterUserHse_FairpriceDT['Distance(M)'] = FilterUserHse_FairpriceDT['Distance (km)'] * 1000
    FilterUserHse_HosDT['Distance(M)'] = FilterUserHse_HosDT['Distance (km)'] * 1000
    FilterUserHse_MallsDT['Distance(M)'] = FilterUserHse_MallsDT['Distance (km)'] * 1000
    FilterUserHse_MRTDT['Distance(M)'] = FilterUserHse_MRTDT['Distance (km)'] * 1000
    FilterUserHse_ParksDT['Distance(M)'] = FilterUserHse_ParksDT['Distance (km)'] * 1000
    FilterUserHse_PriSchDT['Distance(M)'] = FilterUserHse_PriSchDT['Distance (km)'] * 1000
    FilterUserHse_SecSchDT['Distance(M)'] = FilterUserHse_SecSchDT['Distance (km)'] * 1000
    FilterUserHse_TertairyDT['Distance(M)'] = FilterUserHse_TertairyDT['Distance (km)'] * 1000
    FIlterUserHse_UniDT['Distance(M)'] = FIlterUserHse_UniDT['Distance (km)'] * 1000

    
    #Calculate the points
    FilterMDollarHse_FairpriceDT['FairpricePoints'] = Supermarket_MallPoint *( 1 / FilterMDollarHse_FairpriceDT['Distance(M)'])
    FilterMDollarHse_HosDT['HosPoints'] = Hospital_ClinicPoint *( 1 / FilterMDollarHse_HosDT['Distance(M)'])
    FilterMDollarHse_MallsDT['MallPoints'] = Supermarket_MallPoint *( 1 / FilterMDollarHse_MallsDT['Distance(M)'])
    FilterMDollarHse_MRTDT['MRTPoints'] = MRTPoint *( 1 / FilterMDollarHse_MRTDT['Distance(M)'])
    FilterMDollarHse_ParksDT['ParksPoints'] = ParksPoint *( 1 / FilterMDollarHse_ParksDT['Distance(M)'])
    FilterMDollarHse_PriSchDT['PriSchPoints'] = SchoolsPoint *( 1 / FilterMDollarHse_PriSchDT['Distance(M)'])
    FilterMDollarHse_SecSchDT['SecSchPoints'] = SchoolsPoint *( 1 / FilterMDollarHse_SecSchDT['Distance(M)'])
    FilterMDollarHse_TertairyDT['TertairyPoints'] = SchoolsPoint *( 1 / FilterMDollarHse_TertairyDT['Distance(M)'])
    FIlterMDollarHse_UniDT['UniPoints'] = SchoolsPoint *( 1 / FIlterMDollarHse_UniDT['Distance(M)'])

    FilterUserHse_FairpriceDT['FairpricePoints'] = Supermarket_MallPoint *( 1 / FilterUserHse_FairpriceDT['Distance(M)'])
    FilterUserHse_HosDT['HosPoints'] = Hospital_ClinicPoint *( 1 / FilterUserHse_HosDT['Distance(M)'])
    FilterUserHse_MallsDT['MallPoints'] = Supermarket_MallPoint *( 1 / FilterUserHse_MallsDT['Distance(M)'])
    FilterUserHse_MRTDT['MRTPoints'] = MRTPoint *( 1 / FilterUserHse_MRTDT['Distance(M)'])
    FilterUserHse_ParksDT['ParksPoints'] = ParksPoint *( 1 / FilterUserHse_ParksDT['Distance(M)'])
    FilterUserHse_PriSchDT['PriSchPoints'] = SchoolsPoint *( 1 / FilterUserHse_PriSchDT['Distance(M)'])
    FilterUserHse_SecSchDT['SecSchPoints'] = SchoolsPoint *( 1 / FilterUserHse_SecSchDT['Distance(M)'])
    FilterUserHse_TertairyDT['TertairyPoints'] = SchoolsPoint *( 1 / FilterUserHse_TertairyDT['Distance(M)'])
    FIlterUserHse_UniDT['UniPoints'] = SchoolsPoint *( 1 / FIlterUserHse_UniDT['Distance(M)'])


    #Group the amenties points to the coordinates 
    MDollarHse_FairpricePoint = FilterMDollarHse_FairpriceDT.groupby('Coordinates')['FairpricePoints'].sum().reset_index()
    MDollarHse_HosPoint = FilterMDollarHse_HosDT.groupby('Coordinates')['HosPoints'].sum().reset_index()
    MDollarHse_MallsPoint = FilterMDollarHse_MallsDT.groupby('Coordinates')['MallPoints'].sum().reset_index()
    MDollarHse_MRTPoint = FilterMDollarHse_MRTDT.groupby('Coordinates')['MRTPoints'].sum().reset_index()
    MDollarHse_ParksPoint = FilterMDollarHse_ParksDT.groupby('Coordinates')['ParksPoints'].sum().reset_index()
    MDollarHse_PriSchPoint = FilterMDollarHse_PriSchDT.groupby('Coordinates')['PriSchPoints'].sum().reset_index()
    MDollarHse_SecSchPoint = FilterMDollarHse_SecSchDT.groupby('Coordinates')['SecSchPoints'].sum().reset_index()
    MDollarHse_TertairyPoint = FilterMDollarHse_TertairyDT.groupby('Coordinates')['TertairyPoints'].sum().reset_index()
    MDollarHse_UniPoint = FIlterMDollarHse_UniDT.groupby('Coordinates')['UniPoints'].sum().reset_index()

    UserHse_FairpricePoint = FilterUserHse_FairpriceDT.groupby('Coordinates')['FairpricePoints'].sum().reset_index()
    UserHse_HosPoint = FilterUserHse_HosDT.groupby('Coordinates')['HosPoints'].sum().reset_index()
    UserHse_MallsPoint = FilterUserHse_MallsDT.groupby('Coordinates')['MallPoints'].sum().reset_index()
    UserHse_MRTPoint = FilterUserHse_MRTDT.groupby('Coordinates')['MRTPoints'].sum().reset_index()
    UserHse_ParksPoint = FilterUserHse_ParksDT.groupby('Coordinates')['ParksPoints'].sum().reset_index()
    UserHse_PriSchPoint = FilterUserHse_PriSchDT.groupby('Coordinates')['PriSchPoints'].sum().reset_index()
    UserHse_SecSchPoint = FilterUserHse_SecSchDT.groupby('Coordinates')['SecSchPoints'].sum().reset_index()
    UserHse_TertairyPoint = FilterUserHse_TertairyDT.groupby('Coordinates')['TertairyPoints'].sum().reset_index()
    UserHse_UniPoint = FIlterUserHse_UniDT.groupby('Coordinates')['UniPoints'].sum().reset_index()

    #Mergae the dataframe into 1
    MDollarHSe_Meraged_Points = MDollarHse_FairpricePoint.merge(MDollarHse_HosPoint, on='Coordinates', how='outer')
    MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_MallsPoint, on='Coordinates', how='outer')
    MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_MRTPoint, on='Coordinates', how='outer')
    MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_ParksPoint, on='Coordinates', how='outer')
    MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_PriSchPoint, on='Coordinates', how='outer')
    MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_SecSchPoint, on='Coordinates', how='outer')
    MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_TertairyPoint, on='Coordinates', how='outer')
    MDollarHSe_Meraged_Points = MDollarHSe_Meraged_Points.merge(MDollarHse_UniPoint, on='Coordinates', how='outer')

    UserHse_Meraged_Points = UserHse_FairpricePoint.merge(UserHse_HosPoint, on='Coordinates', how='outer')
    UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_MallsPoint, on='Coordinates', how='outer')
    UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_MRTPoint, on='Coordinates', how='outer')
    UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_ParksPoint, on='Coordinates', how='outer')
    UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_PriSchPoint, on='Coordinates', how='outer')
    UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_SecSchPoint, on='Coordinates', how='outer')
    UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_TertairyPoint, on='Coordinates', how='outer')
    UserHse_Meraged_Points = UserHse_Meraged_Points.merge(UserHse_UniPoint, on='Coordinates', how='outer')

    #Replace empty values with 0 
    MDollarHSe_Meraged_Points['FairpricePoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    MDollarHSe_Meraged_Points['HosPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    MDollarHSe_Meraged_Points['MallPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    MDollarHSe_Meraged_Points['MRTPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    MDollarHSe_Meraged_Points['ParksPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    MDollarHSe_Meraged_Points['PriSchPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    MDollarHSe_Meraged_Points['SecSchPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    MDollarHSe_Meraged_Points['TertairyPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    MDollarHSe_Meraged_Points['UniPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)

    UserHse_Meraged_Points['FairpricePoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    UserHse_Meraged_Points['HosPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    UserHse_Meraged_Points['MallPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    UserHse_Meraged_Points['MRTPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    UserHse_Meraged_Points['ParksPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    UserHse_Meraged_Points['PriSchPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    UserHse_Meraged_Points['SecSchPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    UserHse_Meraged_Points['TertairyPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)
    UserHse_Meraged_Points['UniPoints'].replace([np.inf, -np.inf, np.nan], 0, inplace=True)

    #Calculate the total points starting from the thrid column
    MDollarHSe_Meraged_Points['Total_Points'] = MDollarHSe_Meraged_Points.iloc[:, 2:].sum(axis=1)
    UserHse_Meraged_Points['Total_Points'] = UserHse_Meraged_Points.iloc[:, 2:].sum(axis=1)

    #calculate average points
    MDollar_AveragePoint = MDollarHSe_Meraged_Points['Total_Points'].mean()

    print("Average point for the Million Dollar House is: " + str(MDollar_AveragePoint))

    ##Compare all the user address points towards the average points.
    Filtered_UserHse = UserHse_Meraged_Points[UserHse_Meraged_Points['Total_Points'] > MDollar_AveragePoint]

    #Adding 2 Column into FilteredUserHse.csv
    UserFilteredCoordinates = Filtered_UserHse['Coordinates'].to_list()

    # Split the latitude and longitude from the UserFilteredCoordinates list and store them seperately
    SplitLat = [coord.split(', ')[0] for coord in UserFilteredCoordinates]
    SplitLong = [coord.split(', ')[1] for coord in UserFilteredCoordinates]

    # Create 2 list to store the matching datas
    matched_areas = []
    matched_Links = []
    matched_USerHseTypes = []

    # Check if SplitLat and SplitLong match UserHseDF 'Lat' and UserHseDF 'Long' and retrieve the 'Location_Name' & 'Link' Data
    for i in range(len(SplitLat)):
        lat = SplitLat[i]
        long = SplitLong[i]
        for index, row in UserHseDF.iterrows():
            if lat == row['Lat'] and long == row['Long']:
                matched_area = row['Location_Name']
                matched_Link = row['Link']
                matched_USerHseType = row['Location_Type']
                matched_areas.append(matched_area)
                matched_Links.append(matched_Link)
                matched_USerHseTypes.append(matched_USerHseType)

    Filtered_UserHse['Area'] = matched_areas
    Filtered_UserHse['Location_Type'] = matched_USerHseType
    Filtered_UserHse['Link'] = matched_Links

    #Adding 2 col to FilteredMillionDollarHse.CSV
    MillionFilteredCoordinates = MDollarHSe_Meraged_Points['Coordinates'].to_list()

    # Split the latitude and longitude from the UserFilteredCoordinates list and store them seperately
    SplitMillionLat = [coord.split(', ')[0] for coord in MillionFilteredCoordinates]
    SplitMillionLong = [coord.split(', ')[1] for coord in MillionFilteredCoordinates]

    # Create empty lists to store the matching data
    matched_Millionareas = []
    matched_Milliontypes = []

    # Check if SplitLat and SplitLong match UserHseDF 'Lat' and UserHseDF 'Long' and retrieve the 'Location_Name' & 'Location_Type' Data
    for Mlat, Mlong in zip(SplitMillionLat, SplitMillionLong):
        match_found = False
        for index, row in MDollarHseDF.iterrows():
            if Mlat == row['Lat'] and Mlong == row['Long']:
                matched_Millionareas.append(row['Location_Name'])
                matched_Milliontypes.append(row['Location_Type'])
                match_found = True
                break  # Exit inner loop once a match is found

        if not match_found:
            matched_Millionareas.append(None)  # or any placeholder value
            matched_Milliontypes.append(None)  # or any placeholder value

    # Add the new columns to MDollarHSe_Meraged_Points
    MDollarHSe_Meraged_Points['Area'] = matched_Millionareas
    MDollarHSe_Meraged_Points['Location_Type'] = matched_Milliontypes


    #Take only the last 3 column from FilteredMillionDollarHse.CSV
    PercentageCalculationDF = MDollarHSe_Meraged_Points.iloc[:, -3:]

    #Calculate the Average of total points based on the Area and Location_Type
    grouped_Area_HseType = PercentageCalculationDF.groupby(["Area", "Location_Type"])["Total_Points"].mean().reset_index()

    # Merge based on 'Area' and 'Location_Type'
    merged_df = Filtered_UserHse.merge(grouped_Area_HseType, on=['Area', 'Location_Type'], how='left')

    # Rename the 'Total_Points' column
    merged_df.rename(columns={'Total_Points_x': 'Total_Points', 'Total_Points_y': 'History_Avg_Point'}, inplace=True)

    #calculate the accuracy percentage
    merged_df['Percent'] = (merged_df['Total_Points'] / merged_df['History_Avg_Point'] * 100).clip(upper=100)
    merged_df['Percent'] = merged_df['Percent'].apply(lambda x: 100 if x > 100 else x / 2)

    #pass the dataframe into a CSV file
    MDollarHSe_Meraged_Points.to_csv('scripts/algo/Excel/output/FilteredMillionDollarHse.csv', index=True)
    grouped_Area_HseType.to_csv('scripts/algo/Excel/output/ForPredictionHistory.csv', index=True)
    merged_df.to_csv('scripts/algo/Excel/output/FilteredUserHse.csv', index=True)
    print('done')


'''
    Take Past Data Percentage & Current Add them togather based on the type and area and append
    back to file then show it
    Filter - House Type 
    Filter - Best House
    Show Price Prediction For Area Also 
    Create Function : to compare with the million dollar house and get the percentage out and append tot he user house 
    remeber to reduce to 50% each 
'''



# Read the Million Door File (centralized/merger)

def get_data_from_million_door_file():
    df1 = pd.read_csv('Excel/percentage/Cleaned_HistoryData.csv')
    df2 = pd.read_csv('Excel/percentage/FilteredUserHse.csv')


    # Re write the code here
    accuracy_dict = df1.set_index(['Town', 'Flat_Type'])['Accuracy_Percentage'].to_dict()
    df2['Accuracy_Percentage'] = df2.apply(lambda row: accuracy_dict.get((row['Area'], row['Location_Type']), None), axis=1)
    df2.to_csv('Excel/percentage/UpdatedUserHse.csv', index=False)

    # Get both value from the Percent & Accuracy_Percentage = get the total percentage






get_data_from_million_door_file()