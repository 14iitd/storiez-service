import requests
from bs4 import BeautifulSoup
import json
# URL of the page containing the quote

def get(i):
    url = f"https://www.azquotes.com/quote/{i}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the quote text
        quote_text = soup.find(class_='single-quote').text.strip()

        # Extract the author name
        author_name = soup.find(class_='author').text.strip()

        # Print the extracted quote and author

        payload = {"title":quote_text,"texts": [quote_text, author_name],  "lang": "ENGLISH", "loc": "ALL", "cat": "quote",
                   "template": "quote"}
        if len(quote_text)<200:
            res1 = requests.post("https://playchat.live/storiez/post", data=json.dumps(payload))
            print(res1.text)
    else:
        print("Failed to retrieve the webpage.")
for i in range(3726,1000000):
    get(i)
    print(i)