from config import STOCK_SYMBOLS
from fetch_data import fetch_daily_stock, save_data_to_csv, fetch_weekly_stock
from process_data   import  load_and_process_stock_data
from alert  import check_price_alert

import logging
import schedule
import time
from utils import setup_logger
from utils import write_alert_to_report


def run():

    setup_logger()
    logging.info('===Starting stock alert run===')
    for symbol in STOCK_SYMBOLS:
        try:
            print(f"\n[*] Checking {symbol}....")

            daily_df = fetch_daily_stock(symbol)
            save_data_to_csv(symbol,daily_df)

            weekly_df = fetch_weekly_stock(symbol)
            save_data_to_csv(symbol, weekly_df, "weekly")




            processed_df = load_and_process_stock_data(symbol)
            alert = check_price_alert(symbol,processed_df)
            if alert:
                print(alert)
                logging.info(alert)
                write_alert_to_report(symbol, processed_df["price_change_%"].iloc[0])
               
            else:
                print("No significant price movement")
                logging.info(f"{symbol}: no Significant change.")
        except Exception as e:
            print(f"[!] Error processing {symbol}: {e}")

if __name__ == "__main__":
    run()


def run_scheduler():
    schedule.every().day.at("09:00").do(run)
    print("Scheduler started. waiting for the next run")

    while True:
        schedule.run_pending()
        time.sleep(60)


