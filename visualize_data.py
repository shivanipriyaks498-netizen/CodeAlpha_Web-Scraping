
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_books_data.csv")

# Convert ratings into numeric values
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating_Number"] = df["Rating"].map(rating_map)

# Chart 1: Price Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=15, edgecolor="black")
plt.title("Book Price Distribution")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.close()

print("Price chart saved successfully!")

# Chart 2: Rating Distribution
plt.figure(figsize=(8, 5))

rating_order = ["One", "Two", "Three", "Four", "Five"]
rating_counts = df["Rating"].value_counts().reindex(
    rating_order, fill_value=0
)

plt.bar(rating_counts.index, rating_counts.values)
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.close()

print("Rating chart saved successfully!")

# Chart 3: Availability Distribution
plt.figure(figsize=(7, 5))

availability_counts = df["Availability"].value_counts()

plt.pie(
    availability_counts.values,
    labels=availability_counts.index,
    autopct="%1.1f%%"
)

plt.title("Book Availability Distribution")
plt.tight_layout()
plt.savefig("availability_distribution.png")
plt.close()

print("Availability chart saved successfully!")

print("\nAll 3 charts created successfully!")
