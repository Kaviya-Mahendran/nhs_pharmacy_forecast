import pandas as pd
import os


FOLDER_PATH = "data/processed/regions/"

files = os.listdir(FOLDER_PATH)

print(f"🔍 Found {len(files)} files\n")

for file in files:
    if not file.endswith(".csv"):
        continue

    file_path = os.path.join(FOLDER_PATH, file)
    df = pd.read_csv(file_path)

    print(f"\n📂 Checking: {file}")

    # Convert date
    df['date'] = pd.to_datetime(df['date'])

  
    #  Duplicate check
  
    duplicates = df['date'].duplicated().sum()
    print("Duplicate dates:", duplicates)

   
    #  Missing values
   
    missing = df.isnull().sum().sum()
    print("Missing values:", missing)

 
    #  Sort check
    
    if not df['date'].is_monotonic_increasing:
        print("⚠️ Dates not sorted")
    else:
        print("Dates sorted ")


    # Minimum data points
   
    if len(df) < 6:
        print("⚠️ Too few data points (less than 6 months)")
    else:
        print("Data points OK:", len(df))

 
    # Negative values
   
    if (df['quantity'] < 0).any():
        print(" Some, Negative values found")
    else:
        print("No negative values")

print("\n Validation complete!")