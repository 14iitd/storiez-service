import requests
from bs4 import BeautifulSoup
base_url = "https://www.naidunia.com/web-stories"
response = requests.get(base_url)
res1 = response.text
# Define the base URL
soup = BeautifulSoup(res1, 'html.parser')

# Find the <div> with class "web-story-scroll"
#web_story_scroll_div = soup.find('div', class_='webStory')

# Extract URLs from <a> tags inside the <div>
script_tag = soup.find('script', id='__NEXT_DATA__')

# Check if the script tag exists and has content
if script_tag and script_tag.string:
    # Get the JSON data from the script tag
    json_data = script_tag.string
    import json
    # Parse the JSON data
    try:
        parsed_data = json.loads(json_data)
        #print(parsed_data)  # This will print the parsed JSON data
    except json.JSONDecodeError as e:
        print("Error parsing JSON data:", e)
else:
    print("No JSON data found in the script element with id '__NEXT_DATA__'")
items=parsed_data["props"]["pageProps"]["pageData"]
for item in items:
    cat=item["category"].upper()
    url = "https://www.naidunia.com/web-stories/"+item["url"]
    print(cat,url)
    import json
    payload={"url":url,"cat":cat,"lang":"HINDI","loc":"INDIA"}
    res1=requests.post("https://playchat.live/stories/",data=json.dumps(payload))
    print(res1.text)
