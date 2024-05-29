import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://www.abplive.com/web-stories"

# Send a GET request to the website
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all story links and their titles
story_elements = soup.find_all('a', href=True)

# Extract and print the URLs
for element in story_elements:
    href = element['href']
    if '/web-stories/' in href:
        print(len(href))
        if len(href)>50:
            print(href)

            import json
            payload = {"url": href, "cat": "FACT", "lang": "HINDI", "loc": "INDIA"}
            res1 = requests.post("https://playchat.live/stories/", data=json.dumps(payload))
            print(res1.text)
