import os
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def save_top_bottom_products(product_stats, output_path):

    os.makedirs(output_path, exist_ok=True)

    # Top 10
    top10 = product_stats.sort_values('total_sold', ascending=False).head(10)

    plt.figure(figsize=(10, 6))
    plt.barh(top10['product_name'], top10['total_sold'])
    plt.xlabel("Total Sold")
    plt.title("Top 10 Selling Products")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "top_10_products.png"))
    plt.close()

    # Worst 10 (excluding zero sales)
    worst10 = (
        product_stats[product_stats['total_sold'] > 0]
        .sort_values('total_sold', ascending=True)
        .head(10)
    )

    plt.figure(figsize=(10, 6))
    plt.barh(worst10['product_name'], worst10['total_sold'])
    plt.xlabel("Total Sold")
    plt.title("Worst 10 Selling Products")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "worst_10_products.png"))
    plt.close()

    print("Top and bottom product charts saved.")


def save_rating_distribution(df, output_path):

    rating_dist = df['rating'].value_counts().sort_index()

    plt.figure(figsize=(6, 6))
    plt.pie(rating_dist, labels=rating_dist.index, autopct='%1.1f%%')
    plt.title("Distribution of Ratings")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "rating_distribution.png"))
    plt.close()

    print("Rating distribution chart saved.")


def save_category_rating_chart(category_stats, output_path):

    plt.figure(figsize=(8, 5))
    bars = plt.bar(category_stats['category'], category_stats['avg_rating'])

    plt.xlabel("Category")
    plt.ylabel("Average Rating")
    plt.title("Average Rating by Category")

    for bar in bars:
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.05,
            f"{height:.2f}",
            ha='center',
            va='bottom'
        )

    plt.ylim(0, 5)
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "category_avg_rating.png"))
    plt.close()

    print("Category rating chart saved.")


def save_wordcloud(df, output_path):

    text_data = " ".join(df['text'].astype(str))

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white'
    ).generate(text_data)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title("Most Frequent Words in Reviews")
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, "wordcloud.png"))
    plt.close()

    print("Wordcloud saved.")