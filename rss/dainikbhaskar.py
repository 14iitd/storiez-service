url="https://www.bhaskar.com/rss-v1--category-1061.xml"
import xml.etree.ElementTree as ET
import requests
res=requests.get(url)
xml_string = res.text
root = ET.fromstring(xml_string)
items = root.findall('.//item')
import requests
from bs4 import BeautifulSoup
from  templates import  t1,head,slide
import json
import re

for item in items:
    data=t1
    title = item.find('title').text.strip()
    print(title)
    pattern = r'<media:content url="([^"]*)"'
    #import pdb;pdb.set_trace()
    # Find all matches of the pattern in the XML data
    image_url=item.find('.//media:content',{'media': 'http://search.yahoo.com/mrss/'}).get("url")


    # Extract the image URL from the matches

    print(image_url)

    #######
    title1 = head
    title1 = title1.replace("$img1",image_url)
    title1 = title1.replace("$text1", title)
    data = data.replace("$heading", title1)
    #####

    #####
    data=data.replace("$slides","")
    payload = {"content": data}
    #import pdb;pdb.set_trace()
    res1 = requests.post("https://playchat.live/news/232323", data=json.dumps(payload)).text
    import json
    res1=json.loads(res1)
    payload={"url":"https://playchat.live/news/"+res1["id"],"lang":"HINDI","loc":"INDIA","cat":"TOP"}
    res1=requests.post("https://playchat.live/stories/",data=json.dumps(payload))
    print(res1.text)
    print(res1.text)