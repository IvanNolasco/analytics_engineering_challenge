import sqlite3

def validate_data(df, primary_key_cols=None):
    """
    Validates a DataFrame by checking for:
    - Duplicate primary key values (if key columns are specified)
    - Text fields that exceed 256 characters

    Parameters:
        df (pd.DataFrame): The DataFrame to validate.
        primary_key_cols (list of str, optional): List of columns to treat as the primary key.

    Returns:
        bool: True if the DataFrame passes all checks.

    Raises:
        AssertionError: If duplicate primary key rows are found or text fields exceed the length limit.
    """
    if primary_key_cols:
        dupes = df[df.duplicated(subset=primary_key_cols, keep=False)]
        assert dupes.empty, f"❌ Duplicate primary key rows found on {primary_key_cols}:\n{dupes.head()}"

    assert all(
        isinstance(x, str) and len(x) <= 256
        for x in df.select_dtypes(include='object').stack()
    ), "❌ Some text fields exceed 256 characters."

    print("✅ Data validation passed.")
    return True


def save_to_csv(df, path):
    """
    Saves a DataFrame to a CSV file.

    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        path (str): The file path to save the CSV to.

    Returns:
        None
    """
    df.to_csv(path, index=False)
    print(f"📁 Saved CSV to: {path}")


def save_to_sqlite(df, db_path, table_name):
    """
    Saves a DataFrame to a table in a SQLite database.

    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        db_path (str): Path to the SQLite database file.
        table_name (str): The name of the table to write to.

    Returns:
        None
    """
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists='replace', index=False)
    conn.close()
    print(f"🗃️ Saved table '{table_name}' to SQLite database: {db_path}")
