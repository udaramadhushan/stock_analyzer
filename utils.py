import logging
import os
from config import LOGS_PATH

def setup_logger():
    os.makedirs(LOGS_PATH, exist_ok=True)

    logging.basicConfig(

        filename= os.path.join(LOGS_PATH, 'alerts.log'),
        level= logging.INFO,
        format= "%(asctime)s - %(levelname)s - %(message)s",
        datefmt= '%Y-%m-%d %H:%M:%S'

    )