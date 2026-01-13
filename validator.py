import logging

REQUIRED_FIELDS = [
    "Employee ID",
    "First Name",
    "Last Name",
    "Email",
    "Job Title",
    "Phone Number",
    "Hire Date"
]

COLUMN_MAPPING = {
    "Index": "Index",
    "User Id": "Employee ID",
    "First Name": "First Name",
    "Last Name": "Last Name",
    "Email": "Email",
    "Job Title": "Job Title",
    "Phone": "Phone Number"
}

def validate_and_map(df):
    # Rename known columns
    df = df.rename(columns=COLUMN_MAPPING)

    missing_fields = [f for f in REQUIRED_FIELDS if f not in df.columns]

    if missing_fields:
        logging.error(
            f"Missing required fields as per user story: {missing_fields}"
        )

    # Do NOT raise exception
    return df, missing_fields
