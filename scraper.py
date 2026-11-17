
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Store all scraped books
book_data = []

# Website base URL
base_url = "https://books.toscrape.com/"

# Scrape all 50 pages
for page in range(1, 51):

    print(f"Scraping page {page}...")

    # First page has a different URL
    if page == 1:
        url = base_url
    else:
        url = f"{base_url}catalogue/page-{page}.html"

    # Send request
    response = requests.get(url, timeout=20)
    response.raise_for_status()

    # Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all books
    books = soup.find_all("article", class_="product_pod")
    
    print(f"Books found on page {page}: {len(books)}")

    # Extract book information
    for book in books:

        title = book.h3.a["title"]

        price = book.find(
            "p", class_="price_color"
        ).text.strip().replace("Â", "")

        availability = book.find(
            "p", class_="instock availability"
        ).text.strip()

        rating = book.p["class"][1]

        book_data.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating
        })

# Convert data into DataFrame
df = pd.DataFrame(book_data)

# Save all books into CSV
df.to_csv(
    "books_data.csv",
    index=False,
    encoding="utf-8-sig"
)

# Display results
print("\n========== SCRAPING COMPLETED ==========")

print("Total Books Scraped:", len(df))

print("\nFirst 5 Books:")
print(df.head().to_string(index=False))

print("\nCSV file saved successfully!")

# Verify saved CSV file
saved_data = pd.read_csv("books_data.csv")

print("\nCSV Dataset Verification")
print("Total Rows:", len(saved_data))
print("Total Columns:", len(saved_data.columns))

print("\nColumn Names:")
print(saved_data.columns.tolist())

print("\nFirst 5 Records:")
print(saved_data.head())