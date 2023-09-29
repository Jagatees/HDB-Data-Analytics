import requests

AddressArray = []

#API website www.locationiq.com

def GetLongLatFromAddress():
    #LocationIQ API key
    api_key = "pk.02ff73880ec7a133cfe62191e54c3bd1"

    # Initialize an empty list to store the coordinates
    coordinatesLong = []
    coordinatesLat = []

    # Iterate through the addresses and convert them to coordinates
    for address in AddressArray:
        # Construct the API request URL
        url = f"https://us1.locationiq.com/v1/search.php?key={api_key}&q={address}&format=json"
            
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
                    coordinatesLong.append((longitude))
                    coordinatesLat.append((latitude))
                        
                else:
                    print(f"Location not found for address: {address}")
            else:
                print(f"Error: Unable to access the LocationIQ API for address: {address}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
