import pandas as pd
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from haversine import haversine, Unit
from typing_extensions import ParamSpec  # Use typing_extensions instead of typing

# Sample church location data
data = {
    'Postcode': ['EC1A 1BB', 'W1A 0AX', 'SW1A 1AA', 'WC2N 5DU', 'SE1 2QP'],
    'Latitude': [51.5150, 51.5074, 51.5010, 51.5085, 51.5000],
    'Longitude': [-0.1100, -0.1278, -0.1276, -0.1280, -0.1000],
    'Church_Lat': [51.5155, 51.5078, 51.5015, 51.5090, 51.5005],
    'Church_Long': [-0.1105, -0.1282, -0.1280, -0.1285, -0.1005]
}

df = pd.DataFrame(data)

# Function to geocode postcode to latitude and longitude
def geocode_postcode(postcode):
    geolocator = Nominatim(user_agent="nearest_churches")
    location = geolocator.geocode(postcode)
    if location:
        return (location.latitude, location.longitude)
    else:
        raise ValueError(f"Unable to geocode postcode: {postcode}")

# Function to calculate distance between two points using haversine formula
def calculate_distance(user_lat, user_long, church_lat, church_long):
    return haversine((user_lat, user_long), (church_lat, church_long), unit=Unit.KILOMETERS)

# Main function to find nearest churches
def find_nearest_churches(user_postcode, num_churches=3):
    try:
        # Geocode user's postcode
        user_lat, user_long = geocode_postcode(user_postcode)
        
        # Calculate distance to each church
        df['Distance'] = df.apply(lambda row: calculate_distance(user_lat, user_long, row['Church_Lat'], row['Church_Long']), axis=1)
        
        # Sort by distance and get the nearest churches
        nearest_churches = df.sort_values(by='Distance').head(num_churches)
        
        print(f"Nearest {num_churches} churches to {user_postcode}:")
        print(nearest_churches[['Postcode', 'Church_Lat', 'Church_Long', 'Distance']])
        
    except Exception as e:
        print(f"Error: {e}")

# Example usage
user_postcode = input("Enter your postcode: ")
find_nearest_churches(user_postcode)
