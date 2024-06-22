import requests
from bs4 import BeautifulSoup
base_url = "https://m.dailyhunt.in/news/india/english/news"
response = requests.get(base_url)
print(response)
res1 = response.text
import pdb;pdb.set_trace()
# Define the base URL
data=res1.split("window.__STATE = ")[1]
print("1111111",data[:100])
data=data.split('":{"i')[0].strip()
print(data[1:100])
print(data[1:100])
import json
data=json.loads(data)
import pdb;pdb.set_trace()
https://feeds.feedburner.com/ndtvnews-top-stories