# SmartRetail AI — AI-Powered Supermarket Sales Analysis and Prediction

**Project by:** Vaishnavi Dipak Patil  
**Project type:** Data Analytics with AI  
**Purpose:** Analyze supermarket transactions, create clear visualizations, and demonstrate baseline daily-sales forecasting.

## 1. Project description
SmartRetail AI is a Python-based data analytics project that explores supermarket sales records. It checks and cleans the data, summarizes sales by date, city, category and product, creates charts, and trains a baseline machine-learning model to estimate sales for the next 14 days. The project is intended for learning and demonstration; forecast values are estimates and are not guaranteed business outcomes.

## 2. Dataset
The dataset was supplied with the project materials. No verified public download URL was supplied.

- Raw dataset: [`data/raw/supermarket_sales.csv`](data/raw/supermarket_sales.csv)
- Cleaned dataset: [`data/processed/supermarket_sales_clean.csv`](data/processed/supermarket_sales_clean.csv)
- Dataset size: 500 transaction records
- Date range in the supplied data: 1 January 2026 to 1 July 2026
- Main fields include invoice ID, date, branch, city, customer type, gender, product, category, quantity, unit price, payment, rating and sales.

## 3. Technologies used
- Python 3.10+
- pandas and NumPy — data preparation and analysis
- Matplotlib — charts and visualizations
- scikit-learn — baseline sales forecasting
- joblib — saving the trained model
- Jupyter Notebook — notebook-based analysis
- pytest — basic pipeline tests

## 4. Main findings
Based on the supplied dataset:
- Total sales: 244,411.08 (dataset currency units)
- Average transaction sales: 488.82
- Total units sold: 2,768
- Average customer rating: 3.99
- Highest-sales category: Beverages
- Highest-sales city: Mumbai
- Highest-sales product: Cheese

See [`reports/analysis_summary.md`](reports/analysis_summary.md) and [`reports/data_quality_report.md`](reports/data_quality_report.md) for more detail.

## 5. Project structure
```text
SmartRetail-AI/
├── data/
│   ├── raw/supermarket_sales.csv
│   └── processed/supermarket_sales_clean.csv
├── src/
│   ├── inspect_data.py
│   ├── clean_data.py
│   ├── analyze_sales.py
│   ├── forecast_sales.py
│   └── run_pipeline.py
├── outputs/
│   ├── daily_sales.csv
│   ├── sales_by_category.csv
│   ├── sales_by_city.csv
│   ├── sales_by_product.csv
│   ├── sales_forecast_14_days.csv
│   ├── summary.json
│   ├── forecast_metrics.json
│   └── charts/
├── reports/
├── models/daily_sales_forecaster.joblib
├── powerbi/measures.md
├── tests/test_pipeline.py
├── Vaishnavi_Dipak_Patil_SmartRetail_AI.ipynb
├── Vaishnavi_Dipak_Patil_ProjectReport.docx
├── requirements.txt
└── README.md
```

## 6. Installation and run instructions
Install Python 3.10 or newer, then open a terminal in the repository folder.

Create a virtual environment:
```bash
python -m venv .venv
```

Activate it on Windows:
```powershell
.venv\Scripts\activate
```

Activate it on macOS/Linux:
```bash
source .venv/bin/activate
```

Install dependencies and run the full pipeline:
```bash
pip install -r requirements.txt
python src/run_pipeline.py
```

Run tests:
```bash
pytest -q
```

To run the notebook:
```bash
jupyter notebook
```
Then open `Vaishnavi_Dipak_Patil_SmartRetail_AI.ipynb` and run its cells in order.

## 7. Output files
The `outputs/` folder includes:
- daily sales totals
- sales by category, city and product
- 14-day forecast CSV
- summary and forecast evaluation JSON files
- charts for daily sales, category sales and city sales

## 8. Forecast limitations
The data is small and dates are sparse. A simple baseline model cannot reliably capture all real-world demand patterns, seasonality, promotions or external events. Treat predictions as a demonstration of a machine-learning workflow, not as financial or inventory advice.

## 9. Internship submission files
- [`Vaishnavi_Dipak_Patil_SmartRetail_AI.ipynb`](Vaishnavi_Dipak_Patil_SmartRetail_AI.ipynb)
- [`requirements.txt`](requirements.txt)
- [`Vaishnavi_Dipak_Patil_ProjectReport.docx`](Vaishnavi_Dipak_Patil_ProjectReport.docx)
- [`README.md`](README.md)

For GitHub upload steps, see [`GITHUB_UPLOAD_GUIDE.md`](GITHUB_UPLOAD_GUIDE.md).
