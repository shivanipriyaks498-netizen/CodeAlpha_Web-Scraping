
import pandas as pd

# Load scraped dataset
df = pd.read_csv("books_data.csv")

print("Original Dataset Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

# Convert price into numeric values
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("£", "", regex=False)
    .str.replace("Â", "", regex=False)
    .astype(float)
)

# Save cleaned dataset
df.to_csv("cleaned_books_data.csv", index=False)

# Display final results
print("\n========== DATA CLEANING REPORT ==========")

print("Original Rows:", 1000)
print("Cleaned Rows:", len(df))
print("Total Columns:", len(df.columns))

print("\nCleaned Dataset:")
print(df.head())

print("\nCleaned dataset saved successfully!")
