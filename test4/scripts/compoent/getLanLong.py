import requests
import json


API_KEY = "pk.e1b6b31b46f4a037730c34a22ffdd6d3"

lat = []
long = []
lat_long = []

AddressArray = [{
    "Title": "4 Room HDB in 102 Henderson Crescent",
    "Room_Type": "4 Room HDB ",
    "Location": "Singapore, 102 Henderson Crescent",
    "Price": "525000",
    "Links": "https://www.99.co/singapore/sale/property/102-henderson-crescent-hdb-Rs8vFNGCDVfa3krk4wgC8X",
    "Type": "HDB (4S)",
    "Num_Bed": "3",
    "Num_Toilet": "1",
    "Lease": "99 years"
},
    {
        "Title": "4 Room HDB in 671A Edgefield Plains",
        "Room_Type": "4 Room HDB ",
        "Location": "Singapore, 671A Edgefield Pla",
        "Price": "600000",
        "Links": "https://www.99.co/singapore/sale/property/671a-edgefield-plains-hdb-eM4E23YHt5U6Uy7RsnS2Dy",
        "Type": "HDB (4A)",
        "Num_Bed": "3",
        "Num_Toilet": "2",
        "Lease": "99 years"
},
    {
        "Title": "5 Room HDB in 685C Jurong West Central 1",
        "Room_Type": "5 Room HDB ",
        "Location": "Singapore, 685C Jurong West Central 1",
        "Price": "700000",
        "Links": "https://www.99.co/singapore/sale/property/685c-jurong-west-central-1-hdb-NWwCwjD7oexeN5XtYnWxjq",
        "Type": "HDB (5A)",
        "Num_Bed": "3",
        "Num_Toilet": "2",
        "Lease": "99 years"
},]

def GetLongLatFromAddress(location):
    url = f"https://us1.locationiq.com/v1/search.php?key={API_KEY}&q={location}&format=json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: Unable to access the LocationIQ API for address:")
        return ['None','None']
    return data[0]["lat"],data[0]["lon"]



with open('../99co/main_scrapping.json') as f:
   data = json.load(f)


# x = len(data)
x = 3
for index in range(x):
    x = GetLongLatFromAddress(data[index]['Location'])
    print(x)
    print(x[0])
    print(x[1])
    lat.append(x[0])
    long.append(x[1])


