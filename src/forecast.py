import os
import pandas as pd

INPUT_FOLDER = "data/processed/regions/"
OUTPUT_FOLDER = "data/processed/forecasts/"


def forecast_region_file(file_path: str, output_folder: str, window: int = 3) -> str:
    """Create a rolling-average forecast for one regional time-series file."""
    df = pd.read_csv(file_path)
    df["date"] = pd.to_datetime(df["date"])
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df = df.sort_values("date").copy()

    if df.empty:
        raise ValueError(f"No observations found in {file_path}")
    if window < 1 or len(df) < window:
        raise ValueError("Forecast window must be positive and fit within the historical data")

    df["forecast"] = df["quantity"].rolling(window=window).mean()

    last_date = df["date"].max()
    future_dates = pd.date_range(start=last_date, periods=4, freq="ME")[1:]
    last_avg = df["quantity"].tail(window).mean()

    future_df = pd.DataFrame(
        {
            "date": future_dates,
            "quantity": float("nan"),
            "forecast": float(last_avg),
        }
    )

    final_df = pd.concat([df, future_df], ignore_index=True).sort_values("date")

    os.makedirs(output_folder, exist_ok=True)
    output_file = os.path.basename(file_path).replace("_ts.csv", "_forecast.csv")
    output_path = os.path.join(output_folder, output_file)
    final_df.to_csv(output_path, index=False)
    return output_path


def run_forecasts(input_folder: str = INPUT_FOLDER, output_folder: str = OUTPUT_FOLDER) -> None:
    """Forecast every regional CSV in the input directory."""
    os.makedirs(output_folder, exist_ok=True)
    for file in sorted(os.listdir(input_folder)):
        if file.endswith(".csv"):
            forecast_region_file(os.path.join(input_folder, file), output_folder)


if __name__ == "__main__":
    run_forecasts()
