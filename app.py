# ------------------------------------------------------------
# Streamlit App: Monthly Sales Forecasting Dashboard
# Author: Chitra J
# ------------------------------------------------------------

import streamlit as st
import pandas as pd
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent
data_path = BASE_DIR / "data" / "Sample - Superstore.csv"
output_path = BASE_DIR / "output"

# ------------------------------------------------------------
# Page Setup
# ------------------------------------------------------------
st.set_page_config(page_title="Monthly Sales Forecasting", layout="wide")

st.title("📊 Monthly Sales Forecasting Dashboard")
st.markdown("""
This project predicts monthly sales using past data from the **Superstore dataset**.  
The model is built using the **ARIMA** algorithm to understand trends, seasonality, and forecast future sales.
""")

# ------------------------------------------------------------
# Download Source Section
# ------------------------------------------------------------
with open(data_path, "rb") as file:
    st.download_button(
        label="⬇️ Download Source Data (Superstore CSV)",
        data=file,
        file_name="Sample - Superstore.csv",
        mime="text/csv",
    )

st.markdown("---")

# ------------------------------------------------------------
# Tabs for Charts
# ------------------------------------------------------------
tabs = st.tabs([
    "📈 Monthly Trend",
    "📊 Rolling Average",
    "🧩 Decomposition",
    "🔍 Actual vs Predicted",
    "🔮 Future Forecast",
    "📘 Final Combined Chart"
])

# Load and show each chart
chart_files = {
    "📈 Monthly Trend": "trend_chart.png",
    "📊 Rolling Average": "rolling_avg_chart.png",
    "🧩 Decomposition": "decomposition_chart.png",
    "🔍 Actual vs Predicted": "actual_vs_predicted.png",
    "🔮 Future Forecast": "future_forecast_chart.png",
    "📘 Final Combined Chart": "final_forecast_chart.png"
}

for i, tab in enumerate(tabs):
    with tab:
        file_name = chart_files[list(chart_files.keys())[i]]
        chart_path = output_path / file_name
        if chart_path.exists():
            st.image(str(chart_path), use_container_width=True)
        else:
            st.warning(f"{file_name} not found in output folder. Please run forecasting script first.")

# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------
st.markdown("---")
st.caption("Developed by **Chitra J**")
