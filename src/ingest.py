import requests
import pandas as pd
from io import StringIO

url = "https://files.digital.nhs.uk/assets/ods/current/epraccur.csv"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)

if response.status_code != 200:
    raise Exception("Failed to fetch data")

# Convert to DataFrame
df = pd.read_csv(StringIO(response.text))

print(df.head())
print(df.columns)

# Save file
df.to_csv("data/raw/nhs_sample.csv", index=False)