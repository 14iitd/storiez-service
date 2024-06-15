import requests
import xml.etree.ElementTree as ET
import json
# URL of the RSS feed
url = "https://www.livemint.com/rss/news"

# Fetch the RSS feed
response = requests.get(url)
rss_feed = response.content

# Parse the RSS feed
root = ET.fromstring(rss_feed)

# Define namespaces if needed
namespaces = {
    'media': 'http://search.yahoo.com/mrss/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'dc': 'http://purl.org/dc/elements/1.1/'
}

# Iterate through each item in the RSS feed
for item in root.findall('.//item'):
    title = item.find('title').text.strip()
    description = item.find('description').text.strip()
    url = item.find('link').text.strip()
    # Define the namespace
    namespaces = {'media': 'http://search.yahoo.com/mrss/'}

    # Extract the image URL from media:content
    media_content = item.find('media:content', namespaces)
    if media_content is not None:
        image_url = media_content.attrib.get('url')
    if "default" not in image_url:
        payload = {"texts": [title, description], "img": image_url, "url": url, "lang": "ENGLISH", "loc": "INDIA",
                   "cat": "news",
                   "template": "news"}
        print(payload)
        res1 = requests.post("https://playchat.live/storiez/post", data=json.dumps(payload))
        print(res1.text)
        print(res1.text)

