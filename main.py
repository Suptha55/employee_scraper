import logging
from downloader import download_file
from parser import parse_file
from validator import validate_and_map

GOOGLE_DRIVE_URL = (
    "https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download"
)

logging.basicConfig(
    filename="scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_scraper():
    file_path = download_file(GOOGLE_DRIVE_URL)
    df = parse_file(file_path)

    df, missing_fields = validate_and_map(df)

    logging.info("Scraping completed successfully")

    return df, missing_fields


if __name__ == "__main__":
    data, missing = run_scraper()
    print("Scraped columns:", list(data.columns))
    print("Missing required field:", missing)
