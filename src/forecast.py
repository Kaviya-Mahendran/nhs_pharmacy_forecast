import pandas as pd
import os

INPUT_FOLDER = "data/processed/regions/"
OUTPUT_FOLDER = "data/processed/forecasts/"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


files = os.listdir(INPUT_FOLDER)

for file in files:
    if not file.endswith(".csv"):
        continue

    file_path = os.path.join(INPUT_FOLDER, file)
    df = pd.read_csv(file_path)

    print(f"\n Forecasting: {file}")

    # Convert date
    df['date'] = pd.to_datetime(df['date'])

    # Sort
    df = df.sort_values('date')

    
    window = 3  # last 3 months

    df['forecast'] = df['quantity'].rolling(window=window).mean()

    
    last_date = df['date'].max()

    future_dates = pd.date_range(start=last_date, periods=4, freq='ME')[1:]

    last_avg = df['quantity'].tail(window).mean()

    future_df = pd.DataFrame({
        'date': future_dates,
        'quantity': None,
        'forecast': last_avg
    })

   # Fix datatypes FIRST
df['quantity'] = df['quantity'].astype(float)
df['forecast'] = df['forecast'].astype(float)

future_df['quantity'] = future_df['quantity'].astype(float)
future_df['forecast'] = future_df['forecast'].astype(float)

# Combine
final_df = pd.concat([df, future_df], ignore_index=True)

# Optional: sort
final_df = final_df.sort_values('date')

# Save
output_file = file.replace("_ts.csv", "_forecast.csv")
output_path = os.path.join(OUTPUT_FOLDER, output_file)

final_df.to_csv(output_path, index=False)

print(f"✅ Saved forecast: {output_file}")