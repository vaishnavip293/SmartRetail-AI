from pathlib import Path
import json
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data/processed/supermarket_sales_clean.csv'
OUT=ROOT/'outputs'; CHARTS=OUT/'charts'; REPORT=ROOT/'reports/analysis_summary.md'

def analyze():
    df=pd.read_csv(DATA,parse_dates=['Date'])
    OUT.mkdir(exist_ok=True); CHARTS.mkdir(parents=True,exist_ok=True)
    daily=df.groupby('Date',as_index=False).agg(Sales=('Sales','sum'),Transactions=('Invoice ID','nunique'),Units=('Quantity','sum'))
    daily.to_csv(OUT/'daily_sales.csv',index=False)
    by_cat=df.groupby('Category',as_index=False).agg(Sales=('Sales','sum'),Units=('Quantity','sum'),Transactions=('Invoice ID','nunique')).sort_values('Sales',ascending=False)
    by_cat.to_csv(OUT/'sales_by_category.csv',index=False)
    by_city=df.groupby('City',as_index=False).agg(Sales=('Sales','sum'),Transactions=('Invoice ID','nunique')).sort_values('Sales',ascending=False)
    by_city.to_csv(OUT/'sales_by_city.csv',index=False)
    by_product=df.groupby('Product',as_index=False).agg(Sales=('Sales','sum'),Units=('Quantity','sum')).sort_values('Sales',ascending=False)
    by_product.to_csv(OUT/'sales_by_product.csv',index=False)
    daily.set_index('Date')['Sales'].plot(figsize=(10,5),title='Daily Sales');plt.ylabel('Sales');plt.tight_layout();plt.savefig(CHARTS/'daily_sales.png',dpi=150);plt.close()
    by_cat.sort_values('Sales').plot.barh(x='Category',y='Sales',legend=False,figsize=(9,5),title='Sales by Category');plt.xlabel('Sales');plt.tight_layout();plt.savefig(CHARTS/'sales_by_category.png',dpi=150);plt.close()
    by_city.sort_values('Sales').plot.barh(x='City',y='Sales',legend=False,figsize=(9,5),title='Sales by City');plt.xlabel('Sales');plt.tight_layout();plt.savefig(CHARTS/'sales_by_city.png',dpi=150);plt.close()
    summary={'rows':int(len(df)),'unique_invoices':int(df['Invoice ID'].nunique()),'total_sales':round(float(df['Sales'].sum()),2),'average_transaction_value':round(float(df['Sales'].mean()),2),'total_units':int(df['Quantity'].sum()),'average_rating':round(float(df['Rating'].mean()),2),'date_start':str(df['Date'].min().date()),'date_end':str(df['Date'].max().date()),'top_category':str(by_cat.iloc[0]['Category']),'top_city':str(by_city.iloc[0]['City']),'top_product':str(by_product.iloc[0]['Product'])}
    (OUT/'summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    REPORT.write_text('# SmartRetail AI — Analysis Summary\n\n'+'| Metric | Result |\n|---|---:|\n'+''.join(f"| {k.replace('_',' ').title()} | {v} |\n" for k,v in summary.items())+'\nGenerated from the supplied supermarket dataset. These are descriptive results, not proof of future performance.\n',encoding='utf-8')
    print(REPORT.read_text())
if __name__=='__main__': analyze()
