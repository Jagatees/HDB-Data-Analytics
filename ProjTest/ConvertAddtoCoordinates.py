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


NormalAddress = "2450 Ang Mo Kio Avenue 8"
# Convert address to coordinates
AddCoordinates = GetLongLatFromAddress(NormalAddress)

print(AddCoordinates)