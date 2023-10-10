import KerwinFunction
import pandas as pd
import requests
import time

def GetLongLatFromAddress(AddressArray, Filepath):
    #LocationIQ API key
    api_key = "pk.d67416f0ccfa0f9ad6ea725c7984a5bf"

    coordinatesLong = []
    coordinatesLat = []
    FailedAddress = []
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
                    FailedAddress.append((address))
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
    
    print(len(coordinatesLong))
    print(len(coordinatesLat))

    AddressDataFrame = pd.read_csv(Filepath, header=None)
    AddressDataFrame.columns = ['Location_Name', 'Location_Type', 'Blk_No' ,'Address', 'Postal_Code', 'Full_Address', 'Long', 'Lat', 
                                'floor_area_sqm', 'remaining_lease', 'Price', 'Link', 'Leased_Used', 'Num_Bed', 'Num_Toilet']
    AddressDataFrame = AddressDataFrame.drop(0)

    print('AddressDataFrame = '+ str(len(AddressDataFrame)))

    for index, row in AddressDataFrame.iterrows():

        if row['Long'] == 0:
            AddressDataFrame.drop(index, inplace=True)

    AddressDataFrame.to_csv(Filepath, index=False)

CSV = 'ProjTest\\Excel Data\\csv_merged_final.csv'
#Read the CSV File
UserAddressArray = KerwinFunction.ReadCSVFile(CSV)

print(len(UserAddressArray))

GetLongLatFromAddress(UserAddressArray, CSV)

print('Done')