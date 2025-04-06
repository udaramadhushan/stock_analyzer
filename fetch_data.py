from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import os
from config import RAW_DATA_PATH
from config import API_KEY



def fetch_daily_stock(symbol):
    ts = TimeSeries(key=API_KEY, output_format='pandas')
    data,_ = ts.get_daily(symbol=symbol, outputsize = 'compact')
    return data


def save_data_to_csv(symbol, df,  frquency = 'daily'):
    os.makedirs(RAW_DATA_PATH, exist_ok=True)
    file_path = os.path.join(RAW_DATA_PATH, f"{symbol}_{frquency}.csv")
    df.to_csv(file_path)

    print(f"[+] Data saved to {file_path}")

def fetch_weekly_stock(symbol):
    ts = TimeSeries(key=API_KEY,output_format='pandas' )
    data , _ = ts.get_weekly(symbol=symbol)
    return data