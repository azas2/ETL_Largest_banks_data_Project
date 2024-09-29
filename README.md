🏦 Largest Banks Data Extraction Project

This project extracts data on the largest banks from a Wikipedia page, transforms the data, and loads it into both a CSV file and an SQLite database.
📖 Overview

The script performs the following tasks:

    Data Extraction: Scrapes data from a specific Wikipedia page using BeautifulSoup.
    Data Transformation: Cleans and enriches the data, including currency conversion based on exchange rates.
    Data Loading: Saves the transformed data to a CSV file and an SQLite database.
    Data Querying: Allows for querying the database to retrieve insights about the banks.

🔧 Requirements

To run this project, you'll need:

    Python 3.x
    Libraries:
        pandas
        requests
        beautifulsoup4
        sqlite3
        numpy

You can install the required libraries using:

bash

pip install pandas requests beautifulsoup4 numpy

📂 File Structure

    main.py (your script)
    exchange_rate.csv (CSV file containing currency exchange rates)
    Largest_banks_data.csv (output CSV file)
    Banks.db (SQLite database file)
    code_log.txt (log file for tracking progress)

🚀 Getting Started

    Clone this repository or download the script.
    Ensure you have the exchange_rate.csv file in the same directory.
    Run the script:

bash

python main.py

📊 Queries Available

You can run the following queries after loading data into the database:

    View All Data:

    sql

SELECT * FROM Largest_banks;

Average Market Capitalization (in GBP):

sql

SELECT AVG(MC_GBP_Billion) FROM Largest_banks;

Top 5 Banks:

sql

    SELECT Name FROM Largest_banks LIMIT 5;

📜 Logging

All progress and errors are logged in code_log.txt for your reference.
📬 Contact

For questions or feedback, feel free to reach out!
