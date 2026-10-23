from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]; INPUT=ROOT/'data/raw/supermarket_sales.csv'
df=pd.read_csv(INPUT)
print('Shape:',df.shape);print('Columns:',list(df.columns));print('Types:\n',df.dtypes);print('Missing values:\n',df.isna().sum());print('Duplicate invoice IDs:',df['Invoice ID'].duplicated().sum());print('Date range:',df['Date'].min(),'to',df['Date'].max());print('Sales total:',round(df['Sales'].sum(),2));print('Sales arithmetic mismatches:',((df['Quantity']*df['Unit Price']-df['Sales']).abs()>.011).sum())
