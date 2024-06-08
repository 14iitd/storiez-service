import requests
from bs4 import BeautifulSoup
base_url = "https://ndtv.com/webstories"
response = requests.get(base_url)
res1 = response.text
# Define the base URL
soup = BeautifulSoup(res1, 'html.parser')
story_elements = soup.find_all('a', href=True)

# Find the <div> with class "web-story-scroll"
#web_story_scroll_div = soup.find('div', class_='webStory')
for element in story_elements:
    href = element['href']
    if '/webstories/' in href:
        print(len(href))
        if len(href)>80:
            print(href)

            import json
            payload = {"url": href, "cat": "magazine", "lang": "ENGLISH", "loc": "INDIA"}
            res1 = requests.post("https://playchat.live/storiez/post", data=json.dumps(payload))
            print(res1.text)