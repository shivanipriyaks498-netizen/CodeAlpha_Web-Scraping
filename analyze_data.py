
import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_books_data.csv")

# Basic dataset information
print("========== BOOK DATA ANALYSIS ==========")

print("\nTotal Books:", len(df))

# Price analysis
print("\nPRICE ANALYSIS")

print("Average Price: £", round(df["Price"].mean(), 2))
print("Highest Price: £", df["Price"].max())
print("Lowest Price: £", df["Price"].min())

# Most common rating
print("\nRATING ANALYSIS")

print(df["Rating"].value_counts())

# Availability analysis
print("\nAVAILABILITY ANALYSIS")

print(df["Availability"].value_counts())

# Most expensive book
most_expensive = df.loc[df["Price"].idxmax()]

print("\nMost Expensive Book:")
print("Title:", most_expensive["Title"])
print("Price: £", most_expensive["Price"])

# Cheapest book
cheapest = df.loc[df["Price"].idxmin()]

print("\nCheapest Book:")
print("Title:", cheapest["Title"])
print("Price: £", cheapest["Price"])
