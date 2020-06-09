import json

with open('ccData.json') as json_data:
	jsonData = json.load(json_data)
	
for i in jsonData:
	print i['Product']
	print i['Price']