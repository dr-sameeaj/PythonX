# Day 22: Web Scraping - Building Custom Datasets
# Using BeautifulSoup to extract data from HTML.

import requests
from bs4 import BeautifulSoup

# 1. Target URL (A simple, safe site for scraping practice)
url = 'https://archive.org/details/texts'

try:
    # 2. Fetch the page
    response = requests.get(url)
    
    # 3. Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 4. Extract data: Finding all "collection titles"
    # Logic: Search for specific HTML tags and classes
    titles = soup.find_all('div', class_='item-ia')
    
    print(f"🔎 Scraping successful! Found {len(titles)} items.\n")
    
    for i, item in enumerate(titles[:5], 1):
        # Extracting text and cleaning whitespace
        title_text = item.get_text().strip()
        print(f"{i}. {title_text}")

except Exception as e:
    print(f"❌ Scraping error: {e}")