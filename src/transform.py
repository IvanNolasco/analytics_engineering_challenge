import pandas as pd
from dateutil import parser
from pytz import timezone

# Define the timezone for timestamp normalization
MX_TZ = timezone('America/Mexico_City')


def clean_dates(date_str):
    """
    Parses and standardizes a raw date string to ISO format (YYYY-MM-DD).

    Parameters:
        date_str (str): The raw date string.

    Returns:
        str or None: A cleaned date string in ISO format, or None if parsing fails.
    """
    try:
        return parser.parse(str(date_str)).date().isoformat()
    except:
        return None


def clean_timestamps(ts_str):
    """
    Parses and standardizes a raw timestamp string to ISO format with Mexico City time zone.

    Parameters:
        ts_str (str): The raw timestamp string.

    Returns:
        str or None: A localized and formatted timestamp (YYYY-MM-DD HH:MM:SS),
                     or None if parsing fails.
    """
    try:
        dt = parser.parse(str(ts_str))
        localized = MX_TZ.localize(dt) if dt.tzinfo is None else dt.astimezone(MX_TZ)
        return localized.strftime('%Y-%m-%d %H:%M:%S')
    except:
        return None


def transform_users(df):
    """
    Cleans and standardizes the users DataFrame:
    - Drops duplicate user_id rows
    - Standardizes join_date format
    - Truncates name and email fields to 256 characters

    Parameters:
        df (pd.DataFrame): Raw users DataFrame.

    Returns:
        pd.DataFrame: Cleaned users DataFrame.
    """
    df = df.copy()
    df = df.drop_duplicates(subset='user_id', keep='first')
    df['join_date'] = df['join_date'].apply(clean_dates)
    df['name'] = df['name'].astype(str).str.slice(0, 256)
    df['email'] = df['email'].astype(str).str.slice(0, 256)
    return df


def transform_transactions(df):
    """
    Cleans and standardizes the transactions DataFrame:
    - Drops duplicate transaction_id rows
    - Converts timestamps to ISO format in Mexico City timezone
    - Rounds amount to 2 decimal places
    - Truncates transaction_type to 256 characters

    Parameters:
        df (pd.DataFrame): Raw transactions DataFrame.

    Returns:
        pd.DataFrame: Cleaned transactions DataFrame.
    """
    df = df.copy()
    df = df.drop_duplicates(subset='transaction_id', keep='first')
    df['timestamp'] = df['timestamp'].apply(clean_timestamps)
    df['amount'] = df['amount'].round(2)
    df['transaction_type'] = df['transaction_type'].astype(str).str.slice(0, 256)
    return df


def transform_deliveries(df):
    """
    Cleans and standardizes the deliveries DataFrame:
    - Drops duplicate package_id rows
    - Standardizes delivery_date format
    - Trims, uppercases, and truncates courier names
    - Truncates delivery_status to 256 characters

    Parameters:
        df (pd.DataFrame): Raw deliveries DataFrame.

    Returns:
        pd.DataFrame: Cleaned deliveries DataFrame.
    """
    df = df.copy()
    df = df.drop_duplicates(subset='package_id', keep='first')
    df['delivery_date'] = df['delivery_date'].apply(clean_dates)
    df['courier'] = df['courier'].astype(str).str.strip().str.upper().str.slice(0, 256)
    df['delivery_status'] = df['delivery_status'].astype(str).str.slice(0, 256)
    return df

