import requests
from bs4 import BeautifulSoup
base_url = "https://hindi.news18.com/web-stories/"
response = requests.get(base_url)
res1 = response.text
#print(res1)
# Define the base URL
soup = BeautifulSoup(res1, 'html.parser')

# Find the <div> with class "web-story-scroll"
aas = soup.find_all('div', class_='jsx-355817920 slide')

# Extract URLs from <a> tags inside the <div>

for item in aas:
    #print(item)
    url = "https://hindi.news18.com/"+item.find("a")['href']
    category_tag = item.find('span', class_='jsx-355817920 catrgy')
    cat = category_tag.get_text().upper()
    #
    #print(cat,url)
    import json
    payload={"url":url,"cat":cat,"lang":"HINDI","loc":"INDIA"}
    res1=requests.post("https://playchat.live/stories/",data=json.dumps(payload))
    print(res1.text)
