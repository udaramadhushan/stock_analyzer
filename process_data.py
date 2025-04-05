import pandas as pd
import os
from config import RAW_DATA_PATH

def load_and_process_stock_data(symbol):
    file_path = os.path.join(RAW_DATA_PATH, f"{symbol}_daily.csv")
    df = pd.read_csv(file_path, index_col= 0)
    df.sort_index(ascending=False, inplace= True)
    df.columns = [col.split('. ')[1] if '. ' in col else col for col in df.columns]

    df['price_change_%'] = df['close'].pct_change() * 100

    return df