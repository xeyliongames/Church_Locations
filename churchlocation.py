import pandas as pd
from algoliasearch import SearchClient
import uuid

# Initialize Algolia client with your credentials
client = SearchClient.create('Q8M45RCO3N', 'a2f32593e787d19c5f44ce8a38a99f26')

# Create / connect to the index
index = client.init_index('churchlocation')

# Sample church location data
data = {
    'Postcode': ['EC1A 1BB', 'W1A 0AX', 'SW1A 1AA', 'WC2N 5DU', 'SE1 2QP'],
    'Latitude': [51.5150, 51.5074, 51.5010, 51.5085, 51.5000],
    'Longitude': [-0.1100, -0.1278, -0.1276, -0.1280, -0.1000],
    'Church_Lat': [51.5155, 51.5078, 51.5015, 51.5090, 51.5005],
    'Church_Long': [-0.1105, -0.1282, -0.1280, -0.1285, -0.1005]
}

df = pd.DataFrame(data)

# Add unique objectIDs
df['objectID'] = df.index.astype(str)

# Replace the objectID for the first record with the provided UUID
df.loc[0, 'objectID'] = '4fc2be2a-b3a1-470d-af32-893106483aaa'

# Convert to list of dicts for Algolia
objects = df.to_dict(orient='records')

# OPTIONAL: Set faceting settings
index.set_settings({
    'attributesForFaceting': [
        'filterOnly(Postcode)'
    ]
})

# Upload data to Algolia
response = index.save_objects(objects)
response.wait()  # Wait for indexing to complete

print("Data uploaded to Algolia successfully!")

# OPTIONAL: Perform a test search
result = index.search('EC1A')
print("Search result:", result)
