import pandas as pd


def generate_product_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate product-level aggregated statistics.
    """

    print("Generating product statistics...")

    product_stats = (
        df.groupby(['product_id', 'product_name', 'category', 'shop_id'])
        .agg(
            total_sold=('sold', 'sum'),
            avg_rating=('rating', 'mean'),
            review_count=('text', 'count')
        )
        .reset_index()
    )

    product_stats['avg_rating'] = product_stats['avg_rating'].round(2)

    print("Product statistics generated.")

    return product_stats


def generate_category_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate category-level aggregated statistics.
    """

    print("Generating category statistics...")

    category_stats = (
        df.groupby('category')
        .agg(
            total_sold=('sold', 'sum'),
            avg_rating=('rating', 'mean'),
            total_reviews=('text', 'count')
        )
        .reset_index()
    )

    category_stats['avg_rating'] = category_stats['avg_rating'].round(2)

    print("Category statistics generated.")

    return category_stats


def identify_extreme_products(product_stats: pd.DataFrame):
    """
    Identify most positive and most negative product.
    """

    print("Identifying extreme products...")

    positive = (
        product_stats[product_stats['review_count'] >= 10]
        .sort_values(['avg_rating', 'total_sold'], ascending=[False, False])
        .head(1)
    )

    negative = (
        product_stats[product_stats['total_sold'] > 1]
        .sort_values(['avg_rating', 'total_sold'], ascending=[True, True])
        .head(1)
    )

    print("Extreme products identified.")

    return positive, negative