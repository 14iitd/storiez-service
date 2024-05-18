import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://www.aajtak.in/visualstories"

# Send a GET request to the website
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all story links and their categories
stories = soup.find_all('a',href=True)

# Extract and print the URLs and categories
# Extract and print the URLs
for element in stories:
    href = element['href']
    if '/visualstories/' in href:
        if href.startswith('/'):
            href = f"https://www.aajtak.in/{href}"
        print(href)
