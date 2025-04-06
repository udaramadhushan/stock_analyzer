import logging
import os
from config import LOGS_PATH

import csv
from datetime import datetime
from config import REPORTS_PATH
import os

def write_alert_to_report(symbol, change):
    os.makedirs(REPORTS_PATH, exist_ok=True)
    today = datetime.now().strftime("%Y-%m-%d")
    report_file = os.path.join(REPORTS_PATH, f"alert_report_{today}.csv")

    file_exists = os.path.isfile(report_file)

    with open(report_file, mode= 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["symbol", "change (%)", "timestamp"])
        writer.writerow([symbol, f"{change:.2f}", datetime.now().strftime("%Y-%m-%d %H:%M:%S")])

def setup_logger():
    os.makedirs(LOGS_PATH, exist_ok=True)

    logging.basicConfig(

        filename= os.path.join(LOGS_PATH, 'alerts.log'),
        level= logging.INFO,
        format= "%(asctime)s - %(levelname)s - %(message)s",
        datefmt= '%Y-%m-%d %H:%M:%S'

    )