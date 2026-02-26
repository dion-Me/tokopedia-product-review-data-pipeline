import pandas as pd
import os


def extract_data(input_path: str) -> pd.DataFrame:
    """
    Extract raw dataset from CSV file.

    Parameters:
        input_path (str): Path to raw CSV file

    Returns:
        pd.DataFrame: Raw dataset
    """

    print("Starting data extraction...")

    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File not found at path: {input_path}")

    try:
        df = pd.read_csv(input_path)
        print(f"Data successfully loaded. Shape: {df.shape}")
        return df

    except Exception as e:
        raise Exception(f"Error while reading CSV: {e}")