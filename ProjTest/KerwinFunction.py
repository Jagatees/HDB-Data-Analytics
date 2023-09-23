import math
import requests

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

####Test case for function####
#NormalAddress = "2450 Ang Mo Kio Avenue 8"
# Convert address to coordinates
#AddCoordinates = GetLongLatFromAddress(NormalAddress)

#print(AddCoordinates)

def haversine_distance(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Calculate the distance
    distance = R * c

    return distance

####Test case for function####
# Coordinates for location 1
#lat1 = 1.3247
#lon1 = 103.9293

# Coordinates for location 2
#lat2 = 1.3239
#lon2 = 103.9296

# Calculate the distance between the two locations
#distance = haversine_distance(lat1, lon1, lat2, lon2)

#Round up to 2 decimal place
#Distance2Dp = "{:.2f}".format(distance)

#print(str(Distance2Dp) + "Meters")