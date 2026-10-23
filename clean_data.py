from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'data/raw/supermarket_sales.csv'
OUT=ROOT/'data/processed/supermarket_sales_clean.csv'
REQUIRED=['Invoice ID','Date','Branch','City','Customer Type','Gender','Product','Category','Quantity','Unit Price','Payment','Rating','Sales']

def clean_data(input_path=RAW, output_path=OUT):
    df=pd.read_csv(input_path)
    missing=[c for c in REQUIRED if c not in df.columns]
    if missing: raise ValueError(f'Missing required columns: {missing}')
    df=df[REQUIRED].copy()
    df['Date']=pd.to_datetime(df['Date'],errors='coerce')
    for c in ['Quantity','Unit Price','Rating','Sales']:
        df[c]=pd.to_numeric(df[c],errors='coerce')
    df=df.dropna(subset=['Invoice ID','Date','Quantity','Unit Price','Sales'])
    # Trim whitespace in text columns.
    for c in df.select_dtypes(include='object').columns: df[c]=df[c].str.strip()
    # One row per invoice in this supplied transaction-level dataset; keep first and report via QA.
    df=df.drop_duplicates(subset=['Invoice ID'],keep='first')
    df=df[(df['Quantity']>0)&(df['Unit Price']>=0)&(df['Sales']>=0)]
    df['Calculated Sales']=(df['Quantity']*df['Unit Price']).round(2)
    df['Sales Difference']=(df['Sales']-df['Calculated Sales']).round(2)
    df['Year']=df['Date'].dt.year
    df['Month']=df['Date'].dt.strftime('%Y-%m')
    df['Day Name']=df['Date'].dt.day_name()
    df['Day of Week']=df['Date'].dt.dayofweek
    output_path.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(output_path,index=False)
    return df
if __name__=='__main__':
    df=clean_data()
    print(f'Saved {len(df)} cleaned records to {OUT}')
