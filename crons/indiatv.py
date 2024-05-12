import requests
from bs4 import BeautifulSoup
base_url = "https://www.indiatv.in/web-stories"
response = requests.get(base_url)
res1 = response.text
# Define the base URL
soup = BeautifulSoup(res1, 'html.parser')

# Find the <div> with class "web-story-scroll"
web_story_scroll_div = soup.find('div', class_='web-story-scroll')

# Extract URLs from <a> tags inside the <div>
urls = [a['href'] for a in web_story_scroll_div.find_all('a')]
for url in urls:
    import json
    payload={"url":url,"lang":"HINDI","loc":"INDIA","cat":"RANDOM"}
    res1=requests.post("https://playchat.live/stories/",data=json.dumps(payload))
    print(res1.text)