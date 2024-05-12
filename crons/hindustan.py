import requests
from bs4 import BeautifulSoup
base_url = "https://www.livehindustan.com/web-stories/"
headers = {
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-GB,en-IN;q=0.9,en-US;q=0.8,en;q=0.7',
  'cache-control': 'max-age=0',
  'cookie': '_gid=GA1.2.1504962364.1715011031; _domain_fp_id=3a3c12b9-ffd3-46e2-bef4-72b390a8865b; _ht_fp=3a3c12b9-ffd3-46e2-bef4-72b390a8865b; ppid=b3dcfc6feea9983fb10fe88739b97b4e569b22e0d630ee0d4ca538f423d2facb; we_luid=17accfaf6e48f5c4565e064d8c57b2b661588198; welh_cdp=17accfaf6e48f5c4565e064d8c57b2b661588198; _sp_id=amp-Xnmtxbz8R3nBI4XiPcvgFA; _ht_amp=amp-CkUAO4OLGy-7Vg3VE0lUfA; _cb=amp-NuQAo11ynUvNWxnbzphmXg; msuser=amp-IDYUaCT6nBdO4hvEKIV6xg; _cb=amp-NuQAo11ynUvNWxnbzphmXg; lh-location=IN; lh-city=BANGALORE; lh-state=KA; payucdp=true; AMP_TOKEN=%24NOT_FOUND; _sp_ses.c8cf=*; _ga=GA1.1.883306830.1715011031; FCNEC=%5B%5B%22AKsRol8w8EDOB54PFvFdREj2AgPK1zehvgMW6fA8LihUb7nvURaAoqf9mThNyS8ziVbgP4n54kD_hVL_HBegUllOz2jl9WZfFxrfVXtIus_1dZ0W9pIRexXLQETtpQYu9KMAywBX5KYKCK_7nVAIGkw1kYk6ftQJBQ%3D%3D%22%5D%5D; g_oneTapShow=true; _ga_9KQRGQS875=GS1.1.1715100664.3.1.1715100686.38.0.0; _sp_id.c8cf=562606b1-ba64-463f-8e1a-d63d74511477.1715011033.3.1715100698.1715093854.a28c8088-e151-4863-af5b-e67221e12e9d; lh-city=BANGALORE; lh-location=IN; lh-state=KA',
  'priority': 'u=0, i',
  'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"macOS"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}

response = requests.get(base_url,headers=headers)
res1 = response.text
# Define the base URL
soup = BeautifulSoup(res1, 'html.parser')

# Find the <div> with class "web-story-scroll"

web_story_scroll_div = soup.find('ul', id="webStories")

#print(web_story_scroll_div)
# Extract URLs from <a> tags inside the <div>
urls = [a['href'] for a in web_story_scroll_div.find_all('a')]
for url in urls:
    print("https://www.livehindustan.com/web-stories"+url)
    import json
    payload={"url":"https://www.livehindustan.com/web-stories"+url,"lang":"HINDI","loc":"INDIA","cat":"RANDOM"}
    res1=requests.post("https://playchat.live/stories/",data=json.dumps(payload))
    print(res1.text)