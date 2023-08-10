# Web Scraping with Python

This repository contains a Python script that demonstrates web scraping using the `requests` and `BeautifulSoup` libraries to extract main headings from a given article URL.

## Getting Started

To get started with this script, follow the steps below:

1. Clone the repository to your local machine using the following command:
   
   ```
   git clone https://github.com/arbaz686/web-scrapping/.git
   ```


2. Install the required libraries using `pip`:

   ```
   pip install requests
   pip install beautifulsoup4
   ```

4. Open the `web-scrapping.py` file and replace the `article_url` variable with the URL of the article you want to scrape.

5. Run the script:

   ```
   python web-scrapping.py
   ```

## How It Works

The `web-scrapping.py` script performs the following steps:

1. Imports necessary libraries: `requests` for making HTTP requests and `BeautifulSoup` for parsing HTML content.
2. Defines the `article_url` variable as the URL of the article you want to scrape.
3. Fetches the content of the web page using the `requests.get()` method.
4. Checks if the request was successful (status code 200).
5. If successful, parses the HTML content using `BeautifulSoup`.
6. Finds all main headings (h1) in the HTML.
7. Extracts and prints the text from the main headings.

## Notes

- This script is intended for educational purposes and showcases basic web scraping techniques. Please review and adhere to the terms of use of websites you intend to scrape.
- Make sure to install the required libraries before running the script, as mentioned in the "Getting Started" section.

Feel free to explore and modify the script as needed for your projects!
