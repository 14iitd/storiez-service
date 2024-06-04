import requests
from bs4 import BeautifulSoup
base_url = "https://www.prabhatkhabar.com/ampstories"
response = requests.get(base_url)
res1 = response.text
# Define the base URL
soup = BeautifulSoup(res1, 'html.parser')

# Find the <div> with class "web-story-scroll"
#web_story_scroll_div = soup.find('div', class_='webStory')

# Extract URLs from <a> tags inside the <div>
items = soup.find_all('div',class_="tdb_module_loop td_module_wrap td-animation-stack td-meta-info-hide td-cpt-web-story")
#urls = [a['href'] for a in web_story_scroll_div.find_all('a')]
for item in items:
    cat="RANDOM"
    #print(item)
    url = item.find("a")["href"]
    print(cat,url)
    import json
    payload={"url":url,"cat":"magazine","lang":"HINDI","loc":"INDIA"}
    res1=requests.post("https://playchat.live/storiez/post/",data=json.dumps(payload))
    print(res1.text)
