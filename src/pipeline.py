import json
import sys
from src.extract import extract_data
from src.transform import clean_data
from src.analysis import (
    generate_product_stats,
    generate_category_stats,
    identify_extreme_products
)
from src.visualization import (
    save_top_bottom_products,
    save_rating_distribution,
    save_category_rating_chart,
    save_wordcloud
)
from src.load import save_dataframe


def run_pipeline(config_path="config.json"):

    print("Loading configuration...")

    with open(config_path) as f:
        config = json.load(f)

    input_path = config["input_path"]
    output_path = config["output_path"]

    df = extract_data(input_path)

    df_clean = clean_data(df)

    product_stats = generate_product_stats(df_clean)

    category_stats = generate_category_stats(df_clean)

    positive, negative = identify_extreme_products(product_stats)

    save_dataframe(df_clean, output_path, "cleaned_data.csv")
    save_top_bottom_products(product_stats, output_path)
    save_rating_distribution(df_clean, output_path)
    save_category_rating_chart(category_stats, output_path)
    save_wordcloud(df_clean, output_path)
    save_dataframe(product_stats, output_path, "product_stats.csv")
    save_dataframe(category_stats, output_path, "category_stats.csv")
    save_dataframe(positive, output_path, "most_positive_product.csv")
    save_dataframe(negative, output_path, "most_negative_product.csv")

    print("\nPipeline execution completed successfully.")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_pipeline(sys.argv[1])
    else:
        run_pipeline()