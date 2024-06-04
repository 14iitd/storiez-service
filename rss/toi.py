url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
import xml.etree.ElementTree as ET
import requests

res = requests.get(url)
xml_string = res.text
root = ET.fromstring(xml_string)
items = root.findall('.//item')
import requests
from bs4 import BeautifulSoup
from templates import t1, head, slide
import json

for item in items:
    title = item.find('title').text.strip()
    print(title)
    description = item.find('description')
    #import pdb;pdb.set_trace()
    if description.text is None:
        continue
    description=description.text.strip()

    # print(description)
    # import pdb;pdb.set_trace()
    img = item.find("enclosure").get("url")
    print(img)
    data = t1
    #######
    title1 = head
    title1 = title1.replace("$img1", img)
    title1 = title1.replace("$text1", title)
    data = data.replace("$heading", title1)
    #####
    slides = description.split(".")
    fnews = ""
    for item in slides:
        temp = slide
        temp = temp.replace("$img1", img)
        temp = temp.replace("$text1", item)
        fnews = fnews + temp
    data = data.replace("$slides", fnews)
    payload = {"content": data, "lang": "ENGLISH", "loc": "INDIA", "cat": "news"}
    res1 = requests.post("https://playchat.live/storiez/post", data=json.dumps(payload))
