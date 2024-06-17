url = "https://timesofindia.indiatimes.com/rssfeedstopstories.cms"
import xml.etree.ElementTree as ET
import requests
import requests
import requests
from bs4 import BeautifulSoup
import json
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
    description = item.find('description').text
    url = item.find('link').text.strip()
    print(title)

    print()
    if not description:
        continue
    description=description.strip()
    #print(description)
    img=item.find("enclosure").attrib.get('url')
    print(img)
    payload={"texts":[title,description],"img":img,"url":url,"lang":"ENGLISH","loc":"INDIA","cat":"news","template":"news"}
    print(payload)
    res1=requests.post("https://playchat.live/storiez/post",data=json.dumps(payload))
    print(res1.text)
    print(res1.text)

