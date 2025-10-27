# ------------------------------------------------------------
# Streamlit App: Monthly Sales Forecasting Dashboard
# Author: Chitra J
# ------------------------------------------------------------

import streamlit as st
import pandas as pd
from pathlib import Path
import datetime as dt

# Paths
BASE_DIR = Path(__file__).resolve().parent
data_path = BASE_DIR / "data" / "Sample - Superstore.csv"
output_path = BASE_DIR / "output"

# ------------------------------------------------------------
# Page Setup
# ------------------------------------------------------------
st.set_page_config(page_title="Monthly Sales Forecasting", layout="wide")

st.title("📊 Monthly Sales Forecasting Dashboard")
st.markdown(
    """
This project predicts monthly sales using past data from the **Superstore dataset**.  
The model is built using the **ARIMA** algorithm to understand trends, seasonality, and forecast future sales.
"""
)
current_year = dt.datetime.today().year
st.info(f"📅 **Note:** Dataset dates have been adjusted to align with the current year ({current_year}) for demonstration purposes.")

# ------------------------------------------------------------
# Download Source Section (Download + GitHub link side-by-side)
# ------------------------------------------------------------
# Replace the github_url value below with your actual repository URL if it's different.
github_url = "https://github.com/chitra-codes/sales-forecasting"

col1, col2 = st.columns([1, 1])

with col1:
    try:
        with open(data_path, "rb") as file:
            st.download_button(
                label="⬇️ Download Source Data (Superstore CSV)",
                data=file,
                file_name="Sample - Superstore.csv",
                mime="text/csv",
            )
    except FileNotFoundError:
        st.error(f"Source data not found at `{data_path}`. Please ensure the CSV exists in the data folder.")

with col2:
    st.markdown("###")
    # Simple button-like GitHub link (opens in new tab)
    st.markdown(
        f"""
        <a href="{github_url}" target="_blank" style="text-decoration:none">
            <div style="display:inline-block; padding:10px 14px; border-radius:8px; border:1px solid #ddd; background:#f8f8f8;">
                🔗 View source on GitHub
            </div>
        </a>
        """,
        unsafe_allow_html=True,
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