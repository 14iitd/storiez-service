import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://www.jansatta.com/web-stories/"

# Send a GET request to the website
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all story links
story_elements = soup.select('a[href*="/web-stories/"]')

# Extract and print the URLs
for element in story_elements:
    href = element.get('href')
    if href:
        if href.startswith('/'):
            href = f"https://www.jansatta.com{href}"
        print(href)
