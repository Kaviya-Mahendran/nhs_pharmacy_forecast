import pandas as pd
import os


# load data
INPUT_PATH = "data/processed/cleaned_data.csv"
OUTPUT_FOLDER = "data/processed/regions/"

# Create folder if not exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

df = pd.read_csv(INPUT_PATH)

# Convert date
df['date'] = pd.to_datetime(df['date'])

regions = df['row_name'].unique()

print(f"Total regions found: {len(regions)}")


# LOOP THROUGH EACH REGION
for region in regions:
    print(f"\nProcessing: {region}")

    region_df = df[df['row_name'] == region]

    # Aggregate
    ts = (
        region_df
        .groupby('date', as_index=False)['quantity']
        .sum()
        .sort_values('date')
    )

    # Skip if empty
    if ts.empty:
        print("⚠️ No data, skipping")
        continue

    # Clean filename 
    file_name = region.lower().replace(" ", "_") + "_ts.csv"
    output_path = os.path.join(OUTPUT_FOLDER, file_name)

    # Save
    ts.to_csv(output_path, index=False)

    print(f" Saved: {file_name}")

print("\n All regions processed!")