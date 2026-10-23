from clean_data import clean_data
from analyze_sales import analyze
from forecast_sales import run_forecast
if __name__=='__main__':
    clean_data(); print('1/3 Data cleaning complete.')
    analyze(); print('2/3 Sales analysis complete.')
    run_forecast(); print('3/3 Forecasting complete.')
