import requests
from bs4 import BeautifulSoup
base_url = "https://ndtv.in/webstories"
response = requests.get(base_url)
res1 = response.text
# Define the base URL
soup = BeautifulSoup(res1, 'html.parser')

# Find the <div> with class "web-story-scroll"
#web_story_scroll_div = soup.find('div', class_='webStory')

# Extract URLs from <a> tags inside the <div>
items = soup.find_all('div',class_="--ampS-Itm swiper-slide")
#urls = [a['href'] for a in web_story_scroll_div.find_all('a')]
for item in items:
    category_div = item.find('div', class_='--ampS-Lg')
    print(category_div)
    cat = category_div['class'][1].upper()
    if cat=="FEATURE":
        cat="TRENDING"
    url = item.find("a")["href"]
    print(cat,url)
    import json
    payload={"url":url,"cat":"fact","lang":"HINDI","loc":"INDIA"}
    res1=requests.post("https://playchat.live/stories/",data=json.dumps(payload))
    print(res1.text)
