import asyncio
import time
import json
from requests_html import AsyncHTMLSession

# Need add in Same
API_KEY = "pk.e1b6b31b46f4a037730c34a22ffdd6d3"

lat_1 = []
lon_1 = []
lat_lon = []
data = []

async def GetLongLatFromAddress(session, location):
    url = f"https://us1.locationiq.com/v1/search.php?key={API_KEY}&q={location}&format=json"
    response = await session.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]["lat"], data[0]["lon"]
    return 'None', 'None'

async def main_test():
    s = AsyncHTMLSession()
    tasks = [GetLongLatFromAddress(s, item['Location']) for item in data]
    results = await asyncio.gather(*tasks)

    for lat, lon in results:
        lat_1.append(lat)  # This should be lat.append(lat) and lon.append(lon)
        lon_1.append(lon)  # Change 'long' to 'lon' to avoid conflicts with the 'long' variable name

def main():
    print('starting')
    start = time.perf_counter()
    asyncio.run(main_test())
    fin = time.perf_counter() - start
    print('Time Taken : ' + str(fin))

if __name__ == "__main__":
    with open('main_scrapping.json') as f:
        data = json.load(f)
    main()

result_data = [{'lat': lat, 'lon': lon} for lat, lon in zip(lat_1, lon_1)]

with open('location_coordinates.json', 'w') as json_file:
    json.dump(result_data, json_file)

print("Results saved to location_coordinates.json")
