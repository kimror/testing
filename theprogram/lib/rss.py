# Import global packages
import xml.etree.ElementTree as ET
import requests

# Import project packages
import db


# Get RSS feed
r = requests.get("https://www.vg.no/rss/feed/?categories=1068&keywords=&limit=10&format=rss")

# Get the data from the response
data = r.text

# Parse the XML using ElementTree
tree = ET.ElementTree(ET.fromstring(data))

# Get the XML structure
root = tree.getroot()

for item in root.iter('item'):
	for item_child in item:
		if item_child.tag == 'title':
			title = item_child.text
#			print('Title: ' + item_child.text)
		elif item_child.tag == 'description':
			description = item_child.text
#			print('Description: ' + item_child.text)
		elif item_child.tag == 'link':
			link = item_child.text
#			print('Link: ' + item_child.text)
		elif item_child.tag == 'guid':
			external_id = item_child.text
#			print('GUID: ' + item_child.text)
		elif item_child.tag == 'pubDate':
			published_date = item_child.text
#			print('Published: ' + item_child.text)

	db.insert(external_id, title, description, link, published_date)

# external_id, title, description, link, published_date
