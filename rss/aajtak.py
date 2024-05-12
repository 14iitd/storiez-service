url="https://www.aajtak.in/rssfeeds/?id=home"
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
for item in items:
    title = item.find('title').text.strip()
    print(title)
    description = item.find('description').text.strip()
    #print(description)
    soup = BeautifulSoup(item.find('description').text, 'html.parser')
    news=soup.text
    print(news)
    data = t1
    url = item.find("link").text.strip()
    res=requests.get(url).text
    soup1=BeautifulSoup(res,'html.parser')
    #import pdb;pdb.set_trace()
    img=soup1.find("img",class_="lazyload")["data-src"]
    print(img)
    #######
    title1 = head
    title1 = title1.replace("$img1",img)
    title1 = title1.replace("$text1", title)
    data = data.replace("$heading", title1)
    #####
    slides=news.split(".")
    fnews=""
    for item in slides:
        temp=slide
        temp=temp.replace("$img1",img)
        temp=temp.replace("$text1",item)
        fnews=fnews+temp
    data=data.replace("$slides",fnews)
    payload = {"content": data}
    #import pdb;pdb.set_trace()
    res1 = requests.post("https://playchat.live/news/232323", data=json.dumps(payload)).text
    import json
    res1=json.loads(res1)
    payload={"url":"https://playchat.live/news/"+res1["id"],"lang":"HINDI","loc":"INDIA","cat":"TOP"}
    res1=requests.post("https://playchat.live/stories/",data=json.dumps(payload))
    print(res1.text)
    print(res1.text)