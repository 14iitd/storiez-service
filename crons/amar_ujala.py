import requests
from bs4 import BeautifulSoup
base_url = "https://www.amarujala.com/web-stories?src=mainmenu"
response = requests.get(base_url)
res1 = response.text
# Define the base URL
soup = BeautifulSoup(res1, 'html.parser')

# Find the <div> with class "web-story-scroll"
#web_story_scroll_div = soup.find('div', class_='webStory')

# Extract URLs from <a> tags inside the <div>
items = soup.find_all('div',class_="col-xs-6 col-sm-4 col-md-3")
#urls = [a['href'] for a in web_story_scroll_div.find_all('a')]
for item in items:
    cat=item.find("h5").text.upper()
    #print(item)
    url = "https://www.amarujala.com/"+item.find("a")["href"]
    print(cat,url)
    import json
    payload={"url":url,"cat":cat,"lang":"HINDI","loc":"INDIA"}
    res1=requests.post("https://playchat.live/stories/",data=json.dumps(payload))
    print(res1.text)
