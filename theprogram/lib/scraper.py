# Import global packages
from bs4 import BeautifulSoup
import requests
import sys

# Import project packages
import db

result = db.select()

for external_id, in result:
	r = requests.get(external_id)
	print(external_id)

	data = r.text

	soup = BeautifulSoup(data, "html5lib")

	#print(tag.string)

	#print("--- TITLE ---")

	for tag in soup.find_all(class_="_1o64I"):
		title = tag.string
		#print(tag.string)

	#print("--- END TITLE ---")
	#print("")
	#print("--- TEXT ---")

	text = ''

	for tag in soup.find_all(class_="_2gLYl"):
		if tag.string != None:
			text += tag.string

	external_id = str(external_id)
	title = str(title)
	text = str(text)
	#print(tag.string)
	#text = "".join(text_items)
	#print("--- END TEXT ---")

	db.insert2(external_id, title, text)
