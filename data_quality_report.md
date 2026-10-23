# Data Quality Report

Source: `data/raw/supermarket_sales.csv`, extracted from the supplied `SUPER MARKET DATA.pdf`.

Expected fields: Invoice ID, Date, Branch, City, Customer Type, Gender, Product, Category, Quantity, Unit Price, Payment, Rating, Sales.

Initial extraction checks: 500 records, 13 columns, date range 2026-01-01 to 2026-07-01, 173 distinct transaction dates, total Sales 244,411.08, no blank fields reported in the initial extraction, and no arithmetic mismatches using Sales = Quantity × Unit Price within 0.011 tolerance.

Run `python src/inspect_data.py` and `python src/clean_data.py` to repeat checks. Cleaning drops rows with missing key numeric/date fields, duplicate invoice IDs (keeps first), and negative quantity/unit price/sales. Always inspect the original source before using outputs for business decisions.
