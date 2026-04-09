import pandas as pd

# Load data
df = pd.read_csv("data/raw/nhs_data.csv")

# Convert date
df['date'] = pd.to_datetime(df['date'])

# Sort data
df = df.sort_values(by=['row_name', 'date'])

# Basic validation
print("Missing values:\n", df.isnull().sum())
print("Shape:", df.shape)

# Save cleaned data
df.to_csv("data/processed/cleaned_data.csv", index=False)

print("Cleaned data saved!")