import requests
from bs4 import BeautifulSoup
from lxml import etree

import json
# Function to scrape a single riddle page
def extract_riddle_and_answer(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    riddle_element = soup.find('strong', string='Riddle:')
    answer_element = soup.find('strong', string='Answer')

    riddle_text = riddle_element.next_sibling.strip() if riddle_element else None
    answer_text = answer_element.next_sibling.strip() if answer_element else None

    return riddle_text, answer_text

# Function to scrape the sitemap and extract riddles
def scrape_riddles():
    sitemap_url = 'https://www.riddles.com/sitemap/riddles'
    response = requests.get(sitemap_url)
    soup = BeautifulSoup(response.content, 'xml')

    # Extracting all riddle URLs from the sitemap
    riddle_urls = [loc.text for loc in soup.find_all('loc')]
    riddles = []

    for riddle_url in riddle_urls:
        print(riddle_url)
        riddle_id = riddle_url.split('/')[-1]
        riddle, answer = extract_riddle_and_answer(riddle_url)
        print(riddle_id,riddle,answer)
        payload = {"texts": [riddle,answer],"template":"riddle"}
        # import pdb;pdb.set_trace()
        res1 = requests.post("https://playchat.live/news/232323", data=json.dumps(payload)).text
        res1 = json.loads(res1)
        payload = {"url": "https://playchat.live/news/" + res1["id"], "lang": "ENGLISH", "loc": "ALL", "cat": "RIDDLE"}
        res1 = requests.post("https://playchat.live/stories/", data=json.dumps(payload))
    return riddles


scrape_riddles()



