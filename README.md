# NHS Pharmacy Demand Forecasting

This project builds a simple end to end data pipeline to analyse and forecast pharmacy demand using NHS prescribing data.

## Overview
The goal of this project is to understand regional demand patterns and predict future medicine needs to support better resource planning.

## What I Built
- Data ingestion and cleaning using Python
- Transformation of raw data into time series format
- Validation checks for data quality
- Forecasting model using rolling averages
- Visualisation of actual vs predicted demand (Jupyter Notebook)

## Tools & Technologies
- Python (pandas, matplotlib)
- Jupyter Notebook
- CSV datasets (NHS prescribing data)

## Output
- Region wise time series datasets  
- Forecasted demand for future months  
- Visual plots comparing actual vs forecast  

1. Install dependencies:
pip install -r requirements.txt

2. Run scripts:

python src/transform.py
python src/forecast.py

3. Open notebook:

notebooks/analysis.ipynb

## Future Improvements
- Add drug level forecasting for inventory optimisation  
- Use advanced models (ARIMA, Prophet)  
- Build interactive dashboards (Tableau / Power BI)

## Key Learning
This project demonstrates how to move from raw data to insights by building a complete data pipeline and applying time series forecasting.