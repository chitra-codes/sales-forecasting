# 📊 Monthly Sales Forecasting using Time Series Analysis

### 🧠 Overview
This project predicts **future monthly sales** using past sales data from the Superstore dataset.  
It helps understand sales patterns, seasonal behavior, and future trends using a **Time Series Forecasting Model (ARIMA)**.  
All results are visualized through an interactive **Streamlit dashboard**.

> Note:  
> The original dataset (Superstore Sales Data) contains sales records from 2014–2017.  
> To make the model output and dashboard always relevant to the current date,  
> the project includes a **date-shifting logic** that automatically adjusts all dates so that the dataset ends with the current year.  
> This ensures the forecast is always shown for the latest months (e.g., 2025–2026) even though the source data is older.  

---

## 🎯 Project Objectives
- Analyze historical sales and find seasonal trends  
- Build an ARIMA model to predict future sales  
- Visualize all results and forecasts in one simple dashboard  
- Make it easy for others to view and download project outputs

---

## 🧰 Tools and Libraries Used
- **Python 3.8+**  
- **Pandas**, **NumPy** → data handling and analysis  
- **Matplotlib**, **Seaborn** → data visualization  
- **Statsmodels (ARIMA)** → forecasting model  
- **Scikit-learn** → model evaluation metrics (MAE, RMSE)  
- **Streamlit** → web dashboard for visualization  

---

## 📁 Project Structure

SalesForecastingMiniProject/ <br>
│ ├── data/ <br>
│ └── Sample - Superstore.csv <br>
│ ├── notebooks/ <br>
│ └── sales_forecasting.py <br>
│ ├── output/ <br>
│ ├── trend_chart.png <br>
│ ├── rolling_avg_chart.png <br>
│ ├── decomposition_chart.png <br>
│ ├── actual_vs_predicted.png <br>
│ ├── future_forecast_chart.png <br>
│ ├── final_forecast_chart.png <br>
│ ├── future_forecast.csv <br> 
│ └── project_summary.txt <br>
│ ├── app.py <br>
└── README.md <br>

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Download the Repository
<<<<<<< HEAD
git clone https://github.com/chitra-codes/sales-forecasting.git <br>
cd sales-forecasting

### 2️⃣ (Optional) Create a Virtual Environment
python -m venv .venv <br>
.venv\Scripts\activate      # for Windows <br>
source .venv/bin/activate   # for Mac/Linux
=======
git clone https://github.com/chitra-codes/sales-forecasting.git<br>
cd sales-forecasting

### 2️⃣ (Optional) Create a Virtual Environment
python -m venv .venv<br>
.venv\Scripts\activate      # for Windows<br>
source .venv/bin/activate   # for Mac/Linux<br>
>>>>>>> dbdac61f50eb4ee44e452ffa5065aa176fd3511c

### 3️⃣ Install Dependencies
pip install pandas numpy matplotlib seaborn statsmodels scikit-learn streamlit

### 4️⃣ Run the Forecasting Script
This will generate all forecast results and charts inside the `output/` folder.<br>
python notebooks/sales_forecasting.py

### 5️⃣ Launch the Streamlit Dashboard
streamlit run app.py

Open your browser and visit → http://localhost:8501

---

## 🌐 Live Demo
After deploying to **Streamlit Cloud**, your live public link will appear like this:

🔗 **Live App:** https://sales-forecasting-chitra-codes.streamlit.app/

---

## 📈 Model Metrics
| Metric | Description | Example Value |
|--------|--------------|----------------|
| **MAE** | Mean Absolute Error | 2450.23 |
| **RMSE** | Root Mean Squared Error | 3100.45 |

*(Actual values may vary depending on dataset version and parameters.)*

---

## 🧠 Key Learnings
- Preparing and cleaning time-series data for forecasting  
- Understanding trend and seasonality in sales data  
- Building an ARIMA model to predict future sales  
- Evaluating forecast accuracy with MAE and RMSE  
- Deploying a simple Streamlit dashboard for public access  

---

## 👩‍💻 Author
**Chitra J**  
_Data Science Mini Project — Monthly Sales Forecasting_  

---

## 🪪 License
This project is created for learning and educational purposes.  
You are free to reuse or modify it by giving proper credit.
