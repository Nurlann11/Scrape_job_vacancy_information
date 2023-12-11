# Vacancy Data Scraper and Analysis

This repository contains a Python script for scraping job vacancy data from a website and performing data analysis using Selenium and Pandas.

## Script Overview

- **Script File**: [scrape_and_analyze.py](scrape_and_analyze.py)
- **Dependencies**: Selenium, Pandas, psutil, Firefox WebDriver
- **Data Source**: [browser.az/vakansiyalar/](https://browser.az/vakansiyalar/)
- **Output**: [vacancy_browser.csv](vacancy_browser.csv)

## Instructions

1. Install the required Python libraries:
   ```bash
   pip install selenium pandas psutil

Download the Firefox WebDriver and ensure it's in your system's PATH.

Run the script:

bash
Copy code
python scrape_and_analyze.py
The script will scrape job vacancy data, write it to a CSV file, and perform basic data analysis.

## Data Analysis
The script performs the following analyses on the scraped data:

Scrapes job vacancy information (name, date, salary, description, company).
Writes the data to a CSV file (vacancy_browser.csv).
Cleans the data (removes duplicates, handles missing values).
Translates Azeri month names to English and converts date format.
Extracts day, month, and year from the 'vacancy_date' column.
Analyzes the top months and days with the most job vacancies.
Filters jobs with specific keywords (e.g., 'Graphic Designer').
Extracts salary information and categorizes by currency (AZN, EUR, USD).
Repository Structure
scrape_and_analyze.py: Main Python script for scraping and analysis.
vacancy_browser.csv: Output CSV file containing job vacancy data.
README.md: Instructions and overview of the project.
Feel free to explore the script and modify it according to your needs. Happy coding!