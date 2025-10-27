# ------------------------------------------------------------
# Author: Chitra J
# Project: Monthly Sales Forecasting using ARIMA
# Description: This project predicts future sales based on past data.
# ------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_absolute_error, mean_squared_error
import os


# ------------------------------------------------------------
# Helper function: Shift dataset dates to align with current date
# ------------------------------------------------------------
def shift_dates_to_current(df, date_col):
    """
    Shifts all dates in the given column so that the dataset's latest date aligns with today's date.
    Example: if the last date in dataset is 2017-06-25, it becomes today's date (e.g., 2025-10-18),
    and all earlier dates are shifted forward by the same number of days.
    """
    max_date = df[date_col].max()
    today = pd.Timestamp.today().normalize()
    shift_days = (today - max_date).days
    df[date_col] = df[date_col] + pd.to_timedelta(shift_days, unit='D')
    print(f"📅 Dates shifted by {shift_days} days — new max date: {df[date_col].max().date()}")
    return df

# Paths
data_path = "../data/Sample - Superstore.csv"
output_path = "../output"
os.makedirs(output_path, exist_ok=True)

print("Step 1: Importing data...")
data = pd.read_csv(data_path, encoding='latin1')
print("Data loaded successfully!")

# Adjust dates so dataset appears current
data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
data = shift_dates_to_current(data, 'Order Date')


# ------------------------------------------------------------
# Step 2: Clean and prepare monthly sales data
# ------------------------------------------------------------
data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
data = data.dropna(subset=['Order Date'])

# Group by month-end and sum sales
monthly_sales = data.groupby(pd.Grouper(key='Order Date', freq='ME'))['Sales'].sum().reset_index()
monthly_sales.columns = ['Month', 'Total_Sales']

print(" Data cleaned and monthly totals prepared!")

# ------------------------------------------------------------
# Step 3: Explore trends and patterns
# ------------------------------------------------------------

# Monthly sales trend
plt.figure(figsize=(10, 5))
plt.plot(monthly_sales['Month'], monthly_sales['Total_Sales'], marker='o', color='teal')
# plt.title("Monthly Sales Trend")
plt.title(f"Monthly Sales Trend (Up to {pd.Timestamp.today().year})")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)
plt.tight_layout()
plt.savefig(f"{output_path}/trend_chart.png", dpi=300)
plt.close()

# Rolling average (3-month window)
monthly_sales['RollingMean'] = monthly_sales['Total_Sales'].rolling(window=3).mean()
monthly_sales['RollingStd'] = monthly_sales['Total_Sales'].rolling(window=3).std()

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales['Month'], monthly_sales['Total_Sales'], label='Original', color='skyblue')
plt.plot(monthly_sales['Month'], monthly_sales['RollingMean'], label='3-Month Avg', color='red')
plt.title('Sales with 3-Month Moving Average')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_path}/rolling_avg_chart.png", dpi=300)
plt.close()

# Seasonal pattern
monthly_sales.set_index('Month', inplace=True)
result = seasonal_decompose(monthly_sales['Total_Sales'], model='additive', period=12)
result.plot()
plt.tight_layout()
plt.savefig(f"{output_path}/decomposition_chart.png", dpi=300)
plt.close()

print(" EDA charts saved successfully!")

# ------------------------------------------------------------
# Step 4: Train ARIMA model
# ------------------------------------------------------------
train = monthly_sales[:-6]
test = monthly_sales[-6:]

print("Training ARIMA model...")
model = ARIMA(train['Total_Sales'], order=(1, 1, 1))
model_fit = model.fit()
print("Model training done!")

# ------------------------------------------------------------
# Step 5: Evaluate model
# ------------------------------------------------------------
forecast = model_fit.forecast(steps=6)
pred_df = test.copy()
pred_df['Predicted_Sales'] = forecast.values

mae = mean_absolute_error(test['Total_Sales'], pred_df['Predicted_Sales'])
rmse = np.sqrt(mean_squared_error(test['Total_Sales'], pred_df['Predicted_Sales']))

plt.figure(figsize=(10, 5))
plt.plot(train.index, train['Total_Sales'], label='Train')
plt.plot(test.index, test['Total_Sales'], label='Actual')
plt.plot(test.index, pred_df['Predicted_Sales'], label='Predicted', linestyle='--', marker='o')
plt.title("Actual vs Predicted Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_path}/actual_vs_predicted.png", dpi=300)
plt.close()

print(f" Model evaluation complete! MAE={mae:.2f}, RMSE={rmse:.2f}")

# ------------------------------------------------------------
# Step 6: Forecast next 6 months
# ------------------------------------------------------------
future_steps = 6
future_forecast = model_fit.forecast(steps=len(test) + future_steps)

last_date = monthly_sales.index[-1]
future_dates = pd.date_range(last_date, periods=future_steps + 1, freq='ME')[1:]
future_df = pd.DataFrame({'Month': future_dates, 'Forecasted_Sales': future_forecast[-future_steps:].values})

plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales['Total_Sales'], label='Historical', color='blue')
plt.plot(pred_df.index, pred_df['Predicted_Sales'], label='Predicted (Test)', color='orange', linestyle='--', marker='o')
plt.plot(future_df['Month'], future_df['Forecasted_Sales'], label='Future Forecast', color='red', linestyle='--', marker='o')
# plt.title("Sales Forecast - Past, Predicted, and Future")
plt.title(f" Sales Forecast (Up to {pd.Timestamp.today().year})")

plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_path}/future_forecast_chart.png", dpi=300)
plt.close()

# Final combined view
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales['Total_Sales'], label='Historical', color='steelblue', linewidth=2)
plt.plot(pred_df.index, pred_df['Predicted_Sales'], label='Model Forecast', color='darkorange', linestyle='--', marker='o')
plt.plot(future_df['Month'], future_df['Forecasted_Sales'], label='Next 6-Month Forecast', color='crimson', linestyle='--', marker='o')
plt.title("Monthly Sales Forecast (Past → Future)", fontsize=14, weight='bold')
plt.xlabel("Month")
plt.ylabel("Sales Amount")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig(f"{output_path}/final_forecast_chart.png", dpi=300)
plt.close()

print(" Future forecast and charts saved!")

# ------------------------------------------------------------
# Step 7: Save results
# ------------------------------------------------------------
future_df.to_csv(f"{output_path}/future_forecast.csv", index=False)

with open(f"{output_path}/project_summary.txt", "w", encoding="utf-8") as f:
    f.write("Monthly Sales Forecast Project Summary\n")
    f.write(f"MAE: {mae:.2f}\n")
    f.write(f"RMSE: {rmse:.2f}\n\n")
    f.write("Future Forecast (Next 6 Months):\n")
    f.write(future_df.to_string(index=False))

print("\n All charts and outputs saved in the output folder!")
print("Project completed successfully ")
