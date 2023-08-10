import requests
from bs4 import BeautifulSoup

# URL of the article you want to scrape
article_url = 'https://longreads.com/2023/07/20/barbenheimer-reading-list/'

# Fetch the web page content
response = requests.get(article_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all main headings (h1)
    main_headings = soup.find_all(['h1'])

    # Extract the text from the headings and print them
    if main_headings:
        print("Main Headings:")
        for heading in main_headings:
            print(heading.get_text().strip())
    else:
        print("No main headings found in the article.")
else:
    print("Failed to fetch the article. Status code:", response.status_code)

