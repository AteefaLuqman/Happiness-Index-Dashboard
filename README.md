#  World Happiness Index Dashboard (2015)

An interactive dashboard built using Python, Dash, and Plotly to explore the 2015 World Happiness Report. This project was part of my INT 375 coursework at Lovely Professional University.

##  Features

- 📌 Top 10 Happiest vs. Bottom 10 Countries
- 🔥 Correlation Heatmap of happiness-related factors
- 🌍 Regional comparison of happiness and trust
- 🕊️ Freedom vs. Happiness scatter plot
- 💝 Most Generous Nations visualization

##  Tech Stack

- Python (Pandas, NumPy, Seaborn)
- Plotly + Dash
- SciPy for statistical tests (Z-Test, F-Test)

##  Statistical Analysis

- ✅ Z-test (is the global happiness score > 5?)
- ✅ F-test (variance comparison between regions)
- ✅ Outlier detection using IQR
- ✅ Correlation & Covariance matrices

##  Project Structure

📁 Happiness-Index-Dashboard/
│
├── 2015.csv # Dataset
├── happiness_dashboard.py # Main app
├── 12312309 INT 375 Report.docx # Report
├── README.md # Project overview

## 🚀 How to Run

```bash
pip install -r requirements.txt
python happiness_dashboard.py

