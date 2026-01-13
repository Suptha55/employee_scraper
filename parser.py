import pandas as pd
import logging
def parse_file(file_path):
    try:
        df = pd.read_csv(file_path)
        logging.info("File parsed as CSV")
        return df
    except Exception:
        pass

    try:
        df = pd.read_excel(file_path)
        logging.info("File parsed as Excel")
        return df
    except Exception:
        pass

    raise ValueError("Unsupported or unknown file type")
