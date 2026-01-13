import requests
import time
import os
import logging

MAX_RETRIES = 2
DOWNLOAD_PATH = "employee_data.bin"

def download_file(url):
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()

            with open(DOWNLOAD_PATH, "wb") as f:
                f.write(response.content)

            logging.info("File downloaded successfully")
            return DOWNLOAD_PATH

        except Exception as e:
            logging.error(f"Download attempt {attempt} failed: {e}")
            time.sleep(5)

    raise RuntimeError("File download failed after multiple retries")
