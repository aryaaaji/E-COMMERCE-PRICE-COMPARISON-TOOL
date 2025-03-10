"# E-Commerce Price Comparison Tool" 


## Overview
The **Price Comparison Tool** is a Python-based web scraper that compares product prices from **Amazon** and **eBay** to help users find the best deals. The tool uses **BeautifulSoup** for web scraping and fetches live product details based on user input.

## Features
- Searches for a product on **Amazon** and **eBay**.
- Extracts product name and price from both platforms.
- Converts USD prices to INR for easy comparison.
- Provides a price comparison to determine the cheaper option.

## Installation
Before running the script, ensure you have **Python 3** installed on your system. Then, install the required dependencies using:

```sh
pip install requests
pip install beautifulsoup4
```

## Usage
1. Clone the repository or download the script.
2. Run the script using:
   
   ```sh
   python price_comparison.py
   ```
3. Enter the product name when prompted.
4. The tool will fetch and display price details from Amazon and eBay.
5. It will also determine which platform offers the lowest price.

## Files in the Repository
- `price_comparison.py`: Main script to scrape product prices from Amazon and eBay.
- `README.md`: Documentation for the project.

## Notes
- The script relies on web scraping, which means website structure changes may break it.
- **Amazon** uses anti-scraping mechanisms, so results may vary.
- This tool is intended for educational and personal use only.

## License
This project is open-source under the **MIT License**.

## Author
**Arya Aji**

