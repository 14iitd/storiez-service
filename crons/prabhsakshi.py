import requests
from bs4 import BeautifulSoup

# URL of the website
url = "https://webstories.prabhasakshi.com/"

# Send a GET request to the website
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all story links and their category tags
story_elements = soup.select('a[href*="/webstory/"]')  # Select all <a> tags with href containing "/web-stories/"

for element in story_elements:
    href = element.get('href')
    if "webstory" in href:
        href = f"https://webstories.prabhasakshi.com{href}"
        import json
        payload = {"url": href, "cat": "magazine", "lang": "HINDI", "loc": "INDIA"}
        res1 = requests.post("https://playchat.live/storiez/post", data=json.dumps(payload))
        print(res1.text)

