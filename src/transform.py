import pandas as pd


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and normalize raw dataset.

    - Handle missing review text
    - Normalize whitespace
    - Convert rating and sold columns to integer
    - Remove invalid key identifiers
    """

    print("Starting data cleaning...")

    df = df.copy()

    # Clean text column
    df['text'] = (
        df['text']
        .fillna('')
        .str.replace('\n', ' ', regex=False)
        .str.replace('\r', ' ', regex=False)
        .str.strip()
    )

    # Convert rating to integer
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0).astype(int)

    # Convert sold to integer
    df['sold'] = pd.to_numeric(df['sold'], errors='coerce').fillna(0).astype(int)

    # Drop rows with missing key identifiers
    df = df.dropna(subset=['product_id', 'product_name', 'shop_id'])

    print(f"Data cleaning complete. Shape after cleaning: {df.shape}")

    return df