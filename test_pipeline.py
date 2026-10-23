from pathlib import Path
import sys
import pandas as pd
ROOT=Path(__file__).resolve().parents[1];sys.path.insert(0,str(ROOT/'src'))
from clean_data import clean_data
from forecast_sales import make_daily, add_features

def test_clean_data_has_expected_columns():
    df=clean_data()
    for c in ['Invoice ID','Date','Sales','Quantity','Unit Price','Category','City']: assert c in df.columns
    assert len(df)>0

def test_sales_nonnegative():
    df=pd.read_csv(ROOT/'data/processed/supermarket_sales_clean.csv')
    assert (df['Sales']>=0).all()

def test_daily_data_has_contiguous_dates():
    df=pd.read_csv(ROOT/'data/processed/supermarket_sales_clean.csv',parse_dates=['Date'])
    daily=make_daily(df)
    assert len(daily)==(daily['Date'].max()-daily['Date'].min()).days+1

def test_features_not_empty():
    df=pd.read_csv(ROOT/'data/processed/supermarket_sales_clean.csv',parse_dates=['Date'])
    assert len(add_features(make_daily(df)))>0
