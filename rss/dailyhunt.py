import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://m.dailyhunt.in/news/india/english/news?mode=pwa&action=click"

# Send a GET request to the website
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful
import pdb;pdb.set_trace()
# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all article elements (adjust selectors based on actual HTML structure)
articles = soup.find_all('section', class_='sc-dnqmqq eHtJr')  # Example class name

# Extract and print image URLs and heading lines
for article in articles:
    heading = article.find('figcaption').find('h2')  # Example class name
    img = article.find('figure').find("img")  # Example class name

    if heading and img:
        heading_text = heading.get_text(strip=True)
        img_url = img['src']
        print(f"Heading: {heading_text}, Image URL: {img_url}")
