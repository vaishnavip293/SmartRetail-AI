# Power BI dashboard guide and DAX measures

## Load data
1. Run `python src/run_pipeline.py` from the project root.
2. Power BI Desktop → Get Data → Text/CSV → `data/processed/supermarket_sales_clean.csv`.
3. Set Date to Date, Quantity to Whole Number, Unit Price/Sales to Decimal Number, Rating to Decimal Number.
4. Use `Date` for a date slicer. Optional: create a proper Date table and relate it to the sales table.

## Suggested dashboard layout
- KPI cards: Total Sales, Transactions, Units Sold, Average Transaction Value, Average Rating.
- Line chart: Sales by Date.
- Bar chart: Sales by Category.
- Bar chart: Sales by City and Branch.
- Matrix: Product by Category with Sales and Units.
- Donut: Payment method share.
- Slicers: Date, City, Branch, Category, Customer Type, Gender.
- Forecast page: load `outputs/sales_forecast_14_days.csv` separately and show forecast with an explicit educational-baseline disclaimer.

Assume table name is `supermarket_sales_clean` (rename it in Power Query if needed).

```DAX
Total Sales = SUM(supermarket_sales_clean[Sales])
Transactions = DISTINCTCOUNT(supermarket_sales_clean[Invoice ID])
Units Sold = SUM(supermarket_sales_clean[Quantity])
Average Transaction Value = DIVIDE([Total Sales], [Transactions], 0)
Average Rating = AVERAGE(supermarket_sales_clean[Rating])
Average Unit Price = AVERAGE(supermarket_sales_clean[Unit Price])
Sales per Unit = DIVIDE([Total Sales], [Units Sold], 0)
Sales Previous Month = CALCULATE([Total Sales], DATEADD('Date'[Date], -1, MONTH))
Sales MoM Change = [Total Sales] - [Sales Previous Month]
Sales MoM % = DIVIDE([Sales MoM Change], [Sales Previous Month])
```

For time intelligence, create a Date table in Power BI, mark it as the date table, and relate it to the sales Date field. The source only contains Jan–Jul 2026, so trends are descriptive and seasonal conclusions should be cautious.
