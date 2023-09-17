import math

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

# Coordinates for location 1
lat1 = 1.3247
lon1 = 103.9293

# Coordinates for location 2
lat2 = 1.3239
lon2 = 103.9296

# Calculate the distance between the two locations
distance = haversine_distance(lat1, lon1, lat2, lon2)

#Round up to 2 decimal place
Distance2Dp = "{:.2f}".format(distance)

print(str(Distance2Dp) + "Meters")