import pymongo
from pymongo import MongoClient
import xml.etree.ElementTree as ET
from datetime import datetime
db = MongoClient(mongo_uri="mongodb://127.0.0.1:27017")["games"]


COLLECTION_NAME = "stories"
SITEMAP_DIR = "sitemaps/"
SITEMAP_INDEX_FILE = SITEMAP_DIR + "sitemap_index.xml"
ITEMS_PER_SITEMAP = 10000  # Maximum 50,000 URLs per sitemap as per Google guidelines

# Connect to MongoDB

collection = db[COLLECTION_NAME]

# Fetch URLs from MongoDB
documents = collection.find({},{"_id":1,"created_at":1}).sort({"created_at":-1})
#import pdb;pdb.set_trace()
# Function to format date
def format_date(date):
    return date.strftime("%Y-%m-%d")

# Function to create a single sitemap
def create_sitemap(documents, file_path):
    urlset = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for doc in documents:
        url = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url, "loc")
        loc.text = "https://storiez.today?id="+str(doc["_id"])
        if "created_at" in doc:
            lastmod = ET.SubElement(url, "lastmod")

    tree = ET.ElementTree(urlset)
    tree.write(file_path, encoding="utf-8", xml_declaration=True)

# Create directory for sitemaps
import os
os.makedirs(SITEMAP_DIR, exist_ok=True)

# Split documents into chunks and create individual sitemaps
sitemaps = []
chunk = []
for i, doc in enumerate(documents):
    chunk.append(doc)
    if len(chunk) == ITEMS_PER_SITEMAP:
        file_path = f"{SITEMAP_DIR}sitemap_{len(sitemaps) + 1}.xml"
        create_sitemap(chunk, file_path)
        sitemaps.append(file_path)
        chunk = []
# Create a sitemap for any remaining documents
if chunk:
    file_path = f"{SITEMAP_DIR}sitemap_{len(sitemaps) + 1}.xml"
    create_sitemap(chunk, file_path)
    sitemaps.append(file_path)

# Create sitemap index file
sitemapindex = ET.Element("sitemapindex", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
for sitemap in sitemaps:
    sitemap_element = ET.SubElement(sitemapindex, "sitemap")
    loc = ET.SubElement(sitemap_element, "loc")
    loc.text = os.path.abspath(sitemap)
    lastmod = ET.SubElement(sitemap_element, "lastmod")
    lastmod.text = format_date(datetime.now())
tree = ET.ElementTree(sitemapindex)
tree.write(SITEMAP_INDEX_FILE, encoding="utf-8", xml_declaration=True)

print(f"Sitemap index created at {SITEMAP_INDEX_FILE}")
print(f"{len(sitemaps)} sitemaps created.")
