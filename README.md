# 📊 Monthly Sales Forecasting using Time Series Analysis

### 🧠 Overview
This project predicts **future monthly sales** using past sales data from the **Superstore dataset**.  
It helps understand sales patterns, seasonal behavior, and future trends using a **Time Series Forecasting Model (ARIMA)**.  
All results are visualized through an interactive **Streamlit dashboard**.

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

SalesForecastingMiniProject/ 
│ ├── data/ 
│ └── Sample - Superstore.csv 
│ ├── notebooks/ 
│ └── sales_forecasting.py 
│ ├── output/ 
│ ├── trend_chart.png 
│ ├── rolling_avg_chart.png 
│ ├── decomposition_chart.png 
│ ├── actual_vs_predicted.png 
│ ├── future_forecast_chart.png 
│ ├── final_forecast_chart.png 
│ ├── future_forecast.csv 
│ └── project_summary.txt 
│ ├── app.py 
└── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone or Download the Repository
git clone https://github.com/<your-username>/sales-forecasting-mini-project.git
cd sales-forecasting-mini-project

### 2️⃣ (Optional) Create a Virtual Environment
python -m venv .venv
.venv\Scripts\activate      # for Windows
source .venv/bin/activate   # for Mac/Linux

### 3️⃣ Install Dependencies
pip install pandas numpy matplotlib seaborn statsmodels scikit-learn streamlit

### 4️⃣ Run the Forecasting Script
This will generate all forecast results and charts inside the `output/` folder.
python notebooks/sales_forecasting.py

### 5️⃣ Launch the Streamlit Dashboard
streamlit run app.py

Open your browser and visit → http://localhost:8501

---

## 🌐 Live Demo
After deploying to **Streamlit Cloud**, your live public link will appear here:

🔗 **Live App:** https://chitraj-salesforecast.streamlit.app  
*(update this after deployment)*

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
