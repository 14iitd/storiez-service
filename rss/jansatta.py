url="https://www.jansatta.com/shorts/"
import xml.etree.ElementTree as ET
import requests
import requests
from bs4 import BeautifulSoup
import json

# Send a GET request to the website
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all story links
story_elements = soup.find_all('div',class_="shorts_inner_wrapper swiper-slide")

for divs in story_elements:
    item = divs.find('article', class_="shorts_article")
    title = item.find(class_="shorts_top_heading").text.strip()
    print(title)
    img=divs.find("img")["src"]
    print(img)
    url=item.find("a")["href"]
    print(url)
    description = item.find('p',class_="shorts_artcle_summery").text.strip()
    print(description)
    payload = {"texts": [title, description], "img": img, "url": url, "lang": "HINDI", "loc": "INDIA", "cat": "news",
               "template": "news"}
    res1 = requests.post("https://playchat.live/storiez/post", data=json.dumps(payload))
    print(res1.text)
    print(res1.text)