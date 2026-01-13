import pytest
from downloader import download_file
from parser import parse_file
from validator import validate_and_map
import pandas as pd

GOOGLE_DRIVE_URL = (
    "https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download"
)

# Test Case 1: Verify CSV File Download

def test_file_download():
    file_path = download_file(GOOGLE_DRIVE_URL)
    assert file_path is not None


# Test Case 2: Verify CSV File Extraction

def test_file_extraction():
    file_path = download_file(GOOGLE_DRIVE_URL)
    df = parse_file(file_path)

    assert df is not None
    assert not df.empty


# Test Case 3: Validate File Type and Format

def test_file_type_and_format():
    file_path = download_file(GOOGLE_DRIVE_URL)

    try:
        df = parse_file(file_path)
        parsed = True
    except Exception:
        parsed = False

    assert parsed is True


# Test Case 4: Validate Data Structure

def test_data_structure_validation():
    file_path = download_file(GOOGLE_DRIVE_URL)
    df = parse_file(file_path)

    df, missing = validate_and_map(df)

    # Required fields are checked
    assert isinstance(missing, list)


# Test Case 5: Handle Missing or Invalid Data

def test_missing_required_fields():
    file_path = download_file(GOOGLE_DRIVE_URL)
    df = parse_file(file_path)

    df, missing = validate_and_map(df)

    # Source data does not contain Hire Date
    assert "Hire Date" in missing

# MOCK TESTCASE 1 : Hire date is present
def test_validate_with_hire_date_present():
    data = {
        "Employee ID": [1],
        "First Name": ["John"],
        "Last Name": ["Doe"],
        "Email": ["john.doe@example.com"],
        "Job Title": ["Engineer"],
        "Phone Number": ["1234567890"],
        "Hire Date": ["2023-01-01"]
    }

    df = pd.DataFrame(data)

    df, missing = validate_and_map(df)

    # No required fields should be missing
    assert missing == []

# MOCK TESTCASE 2 : Hire date is missing
def test_validate_with_hire_date_missing():
    data = {
        "Employee ID": [1],
        "First Name": ["Jane"],
        "Last Name": ["Smith"],
        "Email": ["jane.smith@example.com"],
        "Job Title": ["Analyst"],
        "Phone Number": ["9876543210"]
    }

    df = pd.DataFrame(data)

    df, missing = validate_and_map(df)

    # Hire Date should be reported as missing
    assert "Hire Date" in missing
