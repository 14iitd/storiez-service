import requests
from bs4 import BeautifulSoup
base_url = "https://hindi.latestly.com/quickly/"
response = requests.get(base_url)
res1 = response.text
# Define the base URL
soup = BeautifulSoup(res1, 'html.parser')

# Find the <div> with class "web-story-scroll"
divs = soup.find('ul', class_='qly-card-title')

# Extract URLs from <a> tags inside the <div>

# Check if the script tag exists and has content
items=divs.find_all('li')
for item in items:
    url = item.find("a")["href"]
    print(url)
    import json
    payload={"url":url,"cat":"fact","lang":"HINDI","loc":"INDIA"}
    res1=requests.post("https://playchat.live/stories/",data=json.dumps(payload))
    print(res1.text)
