import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://www.tv9hindi.com/webstories"

# Send a GET request to the website
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all story links
story_elements = soup.find_all('a', href=True)

# Extract and print the URLs
for element in story_elements:
    href = element['href']
    if '/webstories/' in href:
        if len(href) > 80:
            import json
            print(href)
            payload = {"url": href, "cat": "magazine", "lang": "HINDI", "loc": "INDIA"}
            res1 = requests.post("https://playchat.live/storiez/post", data=json.dumps(payload))
            print(res1.text)
