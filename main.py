from config import STOCK_SYMBOLS
from fetch_data import fetch_daily_stock, save_data_to_csv
from process_data   import  load_and_process_stock_data
from alert  import check_price_alert

import logging
from utils import setup_logger



def run():

    setup_logger()
    logging.info('===Starting stock alert run===')
    for symbol in STOCK_SYMBOLS:
        try:
            print(f"\n[*] Checking {symbol}....")

            df = fetch_daily_stock(symbol)
            save_data_to_csv(symbol,df)
            processed_df = load_and_process_stock_data(symbol)
            alert = check_price_alert(symbol,processed_df)
            if alert:
                print(alert)
                logging.info(alert)
               
            else:
                print("No significant price movement")
                logging.info(f"{symbol}: no Significant change.")
        except Exception as e:
            print(f"[!] Error processing {symbol}: {e}")

if __name__ == "__main__":
    run()

