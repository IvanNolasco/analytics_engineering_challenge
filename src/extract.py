import pandas as pd

def extract(file_path):
    """
    Extracts data from a CSV file into a pandas DataFrame.

    Parameters:
        file_path (str): The path to the CSV file to load.

    Returns:
        pandas.DataFrame: The loaded data.

    Example:
        df = extract("data/users.csv")
    """
    return pd.read_csv(file_path)

