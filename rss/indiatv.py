url="https://www.indiatv.in/rssnews/topstory.xml"
import xml.etree.ElementTree as ET
import requests
res=requests.get(url)
xml_string = res.text
root = ET.fromstring(xml_string)
items = root.findall('.//item')
import requests
from bs4 import BeautifulSoup
from  templates import t1,head,slide
import json
for item in items:
    title = item.find('title').text.strip()
    print(title)
    description = item.find('description').text.strip()
    #print(description)
    soup = BeautifulSoup(item.find('description').text, 'html.parser')
    news=soup.text.strip()
    print(news)
    img=soup.find("img")["src"]
    print(img)
    data = t1
    #######
    title1 = head
    title1 = title1.replace("$img1", img)
    title1 = title1.replace("$text1", title)
    data = data.replace("$heading", title1)
    #####
    slides = news.split(".")
    fnews = ""
    for item in slides:
        temp = slide
        temp = temp.replace("$img1", img)
        temp = temp.replace("$text1", item)
        fnews = fnews + temp
    data = data.replace("$slides", fnews)
    payload={"content": data,"lang":"HINDI","loc":"INDIA","cat":"news"}
    res1=requests.post("https://playchat.live/storiez/post",data=json.dumps(payload))
    print(res1.text)
    print(res1.text)