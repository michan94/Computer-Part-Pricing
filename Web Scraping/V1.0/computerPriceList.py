# Run with following command:
# python computerPriceList.py

# Comparing products from Canada Computers to Memory Express
# CC - https://www.canadacomputers.com/index.php?cPath=179&sf=:
# ME - https://www.memoryexpress.com/Category/HardDrives?InventoryType=InStock&Inventory=VBBC&Search=SSD&PageSize=120

from bs4 import BeautifulSoup
import pprint as pp
import urllib

cc_page = 'source_cc_ssd.htm'
soup = BeautifulSoup(open(cc_page), "html.parser")

#Get content of all under class px-0 col-12 productInfoSearch pt-2
headings = soup.find_all('div', class_='px-0 col-12 productInfoSearch pt-2')

all_info_regular = []

for head in headings:
	name = head.find('a').text.strip()
	price = head.find('strong').text.strip() 
		
	all_info_regular.append( u' '.join((name, " - Price: " + price)).encode('utf-8').strip())

pp.pprint("Canada Computers")	
pp.pprint("SSDs")
pp.pprint(all_info_regular, indent=4)


###########


cc_sale_page = 'source_cc_ssd_sale.htm'
soup = BeautifulSoup(open(cc_sale_page), "html.parser")
sale_headings = soup.find_all('div', class_='px-0 col-12 productInfoSearch pt-2')

all_info_sale = []

for head in sale_headings:
	name = head.find('a').text.strip()
	reg_price = head.find('span', class_='d-sm-block line-height').text.strip()
	sale_price = head.find('span', class_='text-danger d-block mb-0 pq-hdr-product_price line-height').text.strip()
	saving = float(reg_price[1:]) - float(sale_price[1:])
	
	all_info_sale.append( u' '.join((name, " - Regular Price: " + reg_price, "Sale Price: " + sale_price, 'Savings: $' + str(saving))).encode('utf-8').strip())

pp.pprint("On Sale Items")
pp.pprint(all_info_sale, indent = 4)


###########
#audio_url = head.find('source',{'type':'audio/mpeg'}).get('src')

me_page = 'source_me_ssd.htm'
soup = BeautifulSoup(open(me_page), "html.parser")
headings = soup.find_all('div', class_='c-shca-icon-item')

me_all_info_regular = []

for head in headings:
	brand = head.find('div', class_='c-shca-icon-item__body-name').find('img').get('title')
	#brand = head.find('div', class_='c-shca-icon-item__body').find('img').get('title')
	item = head.find('div', class_='c-shca-icon-item__body-name').find('a').text.strip()
	name = str(brand) + " " + str(item)
	price = head.find('div', class_='c-shca-icon-item__summary-regular').text.strip()
	
	me_all_info_regular.append( u' '.join((name, " - Price: " + price[4:])).encode('utf-8').strip())
	
pp.pprint("Memory Express")
pp.pprint("SSDs")
pp.pprint(me_all_info_regular, indent=4)

#soup.find_all('div', class_='c-shca-icon-item c-shca-icon-item--has-sale')

###########

sale_headings = soup.find_all('div', class_='c-shca-icon-item c-shca-icon-item--has-sale')

me_all_info_sale = []

for head in sale_headings:
	brand = head.find('div', class_='c-shca-icon-item__body-name').find('img').get('title')
	item = head.find('div', class_='c-shca-icon-item__body-name').find('a').text.strip()
	name = str(brand) + " " + str(item)
	reg_price = head.find('div', class_='c-shca-icon-item__summary-regular').text.strip()
	sale_price = head.find('div', class_='c-shca-icon-item__summary-list').find('span').text.strip()
	saving = float(reg_price[6:]) - float(sale_price[1:])
#	pp.pprint(reg_price[5:])
#	pp.pprint(sale_price[1:])
	
	me_all_info_sale.append( u' '.join((name, " - Regular Price: " + reg_price[5:], "Sale Price: " + sale_price, 'Savings: $' + str(saving))).encode('utf-8').strip())
#	me_all_info_sale.append( (name, " - Regular Price: " + reg_price[5:], "Sale Price: " + sale_price, 'Savings: $' + str(saving)))
	
pp.pprint("On Sale Items")
pp.pprint(me_all_info_sale, indent=4)






