url="https://www.indiatv.in/rssnews/topstory.xml"
import xml.etree.ElementTree as ET
import requests
res=requests.get(url)
xml_string = res.text
root = ET.fromstring(xml_string)
items = root.findall('.//item')
import requests
from bs4 import BeautifulSoup
import json
for item in items:
    title = item.find('title').text.strip()
    url = item.find('link').text.strip()
    print(title)
    description = item.find('description').text.strip()
    #print(description)
    soup = BeautifulSoup(item.find('description').text, 'html.parser')
    news=soup.text.strip()
    print(news)
    img=soup.find("img")["src"]
    print(img)
    payload={"texts":[title,news],"img":img,"url":url,"lang":"HINDI","loc":"INDIA","cat":"news","template":"news"}
    res1=requests.post("https://playchat.live/storiez/post",data=json.dumps(payload))
    print(res1.text)
    print(res1.text)