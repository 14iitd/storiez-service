import requests
import xml.etree.ElementTree as ET

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
    enclosure = item.find('media:content')
    img_url = enclosure.get('url') if enclosure is not None else 'No image available'

    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Image URL: {img_url}")
    print()

