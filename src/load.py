import os
import pandas as pd


def save_dataframe(df: pd.DataFrame, output_path: str, filename: str):
    """
    Save dataframe to CSV inside output directory.
    """

    os.makedirs(output_path, exist_ok=True)

    full_path = os.path.join(output_path, filename)

    df.to_csv(full_path, index=False)

    print(f"Saved: {full_path}")