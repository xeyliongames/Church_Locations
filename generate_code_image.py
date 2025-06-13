from Pillow import Image
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import ImageFormatter
from io import BytesIO

# Python code to convert to image
code = """
import pandas as pd
from geopy.geocoders import Nominatim
from haversine import haversine, Unit

# Sample church location data
data = {
    'Postcode': ['EC1A 1BB', 'W1A 0AX'],
    'Church_Lat': [51.5155, 51.5078],
    'Church_Long': [-0.1105, -0.1282],
}

df = pd.DataFrame(data)

def geocode_postcode(postcode):
    geolocator = Nominatim(user_agent="nearest_churches")
    location = geolocator.geocode(postcode)
    return location.latitude, location.longitude if location else None

def find_nearest_churches(user_postcode):
    user_lat, user_long = geocode_postcode(user_postcode)
    if not user_lat:
        print("Postcode not found!")
        return
    df['Distance'] = df.apply(lambda row: haversine((user_lat, user_long), (row['Church_Lat'], row['Church_Long']), unit=Unit.KILOMETERS), axis=1)
    nearest = df.nsmallest(3, 'Distance')
    print(f"Nearest churches to {user_postcode}:\\n{nearest}")

find_nearest_churches('EC1A 1BB')
"""

# Create an ImageFormatter without specifying font_name to avoid fc-list dependency
formatter = ImageFormatter(font_size=14, line_numbers=True)
lexer = PythonLexer()

# Get highlighted code as binary image data
image_bytes = highlight(code, lexer, formatter)

# Load image from bytes
image = Image.open(BytesIO(image_bytes))

# Resize as needed
image = image.resize((780, 580))

# Save the final image
image.save("python_code_image.png")
print("Code image saved as 'python_code_image.png'")