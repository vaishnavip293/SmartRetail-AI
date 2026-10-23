from pathlib import Path
import json
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data/processed/supermarket_sales_clean.csv'; OUT=ROOT/'outputs'; MODEL=ROOT/'models/daily_sales_forecaster.joblib'

def make_daily(df):
    dates=pd.date_range(df['Date'].min(),df['Date'].max(),freq='D')
    daily=df.groupby('Date')['Sales'].sum().reindex(dates,fill_value=0).rename('Sales').to_frame()
    daily.index.name='Date'
    return daily.reset_index()
def add_features(d):
    d=d.copy();d['dow']=d['Date'].dt.dayofweek;d['month']=d['Date'].dt.month;d['dayofyear']=d['Date'].dt.dayofyear
    for lag in [1,7,14,28]:d[f'lag_{lag}']=d['Sales'].shift(lag)
    d['rolling7']=d['Sales'].shift(1).rolling(7).mean()
    return d.dropna().reset_index(drop=True)
def run_forecast(horizon=14):
    df=pd.read_csv(DATA,parse_dates=['Date']); daily=make_daily(df); feat=add_features(daily)
    if len(feat)<45: raise ValueError('Not enough daily history to train a basic forecasting model (need at least 45 feature-ready days).')
    features=['dow','month','dayofyear','lag_1','lag_7','lag_14','lag_28','rolling7']
    split=max(int(len(feat)*0.8),1); train=feat.iloc[:split]; test=feat.iloc[split:]
    model=RandomForestRegressor(n_estimators=300,random_state=42,min_samples_leaf=2)
    model.fit(train[features],train['Sales'])
    pred=model.predict(test[features]) if len(test) else np.array([])
    metrics={'train_rows':int(len(train)),'test_rows':int(len(test)),'MAE':round(float(mean_absolute_error(test['Sales'],pred)),2) if len(test) else None,'RMSE':round(float(np.sqrt(mean_squared_error(test['Sales'],pred))),2) if len(test) else None,'warning':'Short, sparse transaction history; forecast is an educational baseline and should not be used alone for inventory or financial decisions.'}
    # Refit on all feature-ready history then recursive forecast from daily series.
    final=RandomForestRegressor(n_estimators=300,random_state=42,min_samples_leaf=2).fit(feat[features],feat['Sales'])
    MODEL.parent.mkdir(parents=True,exist_ok=True);joblib.dump({'model':final,'features':features},MODEL)
    history=daily.copy(); forecasts=[]
    for _ in range(horizon):
        date=history['Date'].max()+pd.Timedelta(days=1)
        sales=history.set_index('Date')['Sales']
        row={'Date':date,'dow':date.dayofweek,'month':date.month,'dayofyear':date.dayofyear,'lag_1':float(sales.iloc[-1]),'lag_7':float(sales.iloc[-7]) if len(sales)>=7 else float(sales.mean()),'lag_14':float(sales.iloc[-14]) if len(sales)>=14 else float(sales.mean()),'lag_28':float(sales.iloc[-28]) if len(sales)>=28 else float(sales.mean()),'rolling7':float(sales.iloc[-7:].mean())}
        value=max(0,float(final.predict(pd.DataFrame([{k:row[k] for k in features}]))[0])); row['Forecast Sales']=round(value,2); forecasts.append(row);history=pd.concat([history,pd.DataFrame([{'Date':date,'Sales':value}])],ignore_index=True)
    OUT.mkdir(exist_ok=True); pd.DataFrame(forecasts)[['Date','Forecast Sales']].to_csv(OUT/'sales_forecast_14_days.csv',index=False)
    (OUT/'forecast_metrics.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
    print(json.dumps(metrics,indent=2));print(f'Forecast saved: {OUT / "sales_forecast_14_days.csv"}')
if __name__=='__main__': run_forecast()
