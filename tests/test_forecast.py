import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from forecast import forecast_region_file


def test_forecast_creates_future_rows(tmp_path):
    source = tmp_path / "region_ts.csv"
    pd.DataFrame(
        {
            "date": pd.date_range("2026-01-31", periods=4, freq="ME"),
            "quantity": [100, 120, 110, 130],
        }
    ).to_csv(source, index=False)

    output = forecast_region_file(str(source), str(tmp_path / "forecasts"), window=3)
    result = pd.read_csv(output)

    assert len(result) == 7
    assert result["forecast"].notna().sum() >= 2
    assert result["date"].is_monotonic_increasing
