import pandas as pd
import os
from config import RAW_DATA_PATH

def load_and_process_stock_data(symbol, frequencey= 'daily'):
    file_path = os.path.join(RAW_DATA_PATH, f"{symbol}_{frequencey}.csv")
    df = pd.read_csv(file_path, index_col= 0)
    df.sort_index(ascending=False, inplace= True)
    df.columns = [col.split('. ')[1] if '. ' in col else col for col in df.columns]

    df['price_change_%'] = df['close'].pct_change() * 100

    return df

def get_average_close(df):
    return df['close'].mean()


def get_highest_volume_week(df):
    row = df.loc[df['volume'].idxmax()]
    return row.name, row['volume']

def get_price_drops(df, threshold = 5):
    drops = df[df['price_change_%'] < -threshold]
    return drops[['close','price_change_%']]


def get_change_tuples(df):
    return list(df['price_change_%'].items())



