# CodeAlpha Web Scraping Project

## Project Overview
This project is developed as part of the CodeAlpha Data Analytics Internship.

It uses Python web scraping techniques to collect book information from the Books to Scrape website.

The extracted data is cleaned, analyzed, and visualized to understand book prices, ratings, and availability.

## Website
https://books.toscrape.com/

## Technologies Used
- Python 3.14.7
- Requests
- BeautifulSoup
- Pandas
- Matplotlib
- VS Code

## Project Features
- Scrapes book information from 50 website pages.
- Collects 1,000 book records.
- Extracts book titles, prices, availability, and ratings.
- Saves raw data in CSV format.
- Cleans and validates the dataset.
- Performs statistical analysis.
- Creates three data visualizations.

## Dataset Columns
1. Title
2. Price
3. Availability
4. Rating

## Project Files
- `scraper.py` – Extracts book information.
- `clean_data.py` – Cleans the scraped dataset.
- `analyze_data.py` – Performs data analysis.
- `visualize_data.py` – Creates charts.
- `books_data.csv` – Original scraped dataset.
- `cleaned_books_data.csv` – Cleaned dataset.
- `price_distribution.png` – Price visualization.
- `rating_distribution.png` – Rating visualization.
- `availability_distribution.png` – Availability visualization.

## Analysis Results
- Total Books Scraped: 1,000
- Average Book Price: £35.07
- Highest Book Price: £59.99
- Lowest Book Price: £10.00
- Total Books In Stock: 1,000

## Visualizations
The project generates three charts:
1. Book Price Distribution
2. Book Rating Distribution
3. Book Availability Distribution

## How to Run

### 1. Clone the repository
```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the scraper
```bash
python scraper.py
```

### 4. Clean the dataset
```bash
python clean_data.py
```

### 5. Analyze the dataset
```bash
python analyze_data.py
```

### 6. Generate visualizations
```bash
python visualize_data.py
```

## Internship
Developed as part of the CodeAlpha Data Analytics Internship.

## Author
Your Name
=======
# CodeAlpha_Web-Scraping
Python web scraping project using BeautifulSoup, Requests, Pandas, and Matplotlib to collect, clean, analyze, and visualize 1,000 book records.
>>>>>>> 2e213766684fb51b2e82a72244f0414bfc662c28
