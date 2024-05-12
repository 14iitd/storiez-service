import requests
url = "https://api.makestories.io/v2/channel/-ND3GJ4DtSMAgv4RoatO/stories?per_page=30&page=1"
res=requests.get(url).json()
for item in res["stories"]:
    print(item["url"])
    #print(item)
    import json
    payload={"url":item["url"],"lang":"HINDI","loc":"INDIA","cat":"RANDOM"}
    res1=requests.post("https://playchat.live/stories/",data=json.dumps(payload))
    print(res1.text)
