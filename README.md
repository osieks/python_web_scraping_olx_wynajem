# Web Scraper for OLX Real Estate Listings

This is a Python script that scrapes real estate listings from OLX. It uses Selenium for web scraping.
Python code for scraping data from olx www.olx.pl/nieruchomosci/mieszkania/wynajem/gliwice with specific search filters.
Additionally going into each listing and getting data from the inside. 
Mainly done because price in the listing doesn't include administration cost that is shown once clicked on listing.

## Features

- Scrapes real estate listings from a specific OLX URL
- Collects data such as the listing ID, link, title, price, additional rent, and description
- Handles pagination to scrape multiple pages of listings
- Exports the scraped data to an Excel file

## Usage

1. Set the `urlpage` variable to the URL of the OLX page you want to scrape.
2. Run the script with `python script.py`.
3. The script will print the progress to the console and save the results to `output.xlsx`.

## Requirements

- Python 3
- Selenium
- pandas

## Disclaimer

This script is for educational purposes only. Always respect the terms of service of the website you are scraping.

## License

MIT

output in files and on:
https://docs.google.com/spreadsheets/d/e/2PACX-1vQrLOY7YYaMBq0r51dmbqj4Sl7OcTrety2MhK5IuDnAE3I0GJFD2PTYTHGxJaQ0rbHq9js7DuIgnPXZ/pubhtml?gid=1816060064&single=true
