import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = "https://books.toscrape.com/" # "https://www.docstring.fr/api/books_to_scrape/index.html"

try:
	response = requests.get(url)
	#print(response)  or print(response.status_code) #200
	#print(response.text) # return code html 

	response.raise_for_status #200
except requests.exceptions.HTTPError as errh:
	print("Http Error:", errh)
except requests.exceptions.ConnectionError as errc:
	print("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
	print("Timout Error:", errt)
except requests.exceptions.RequestException as err:
	print("OOps: Something Else", err)

#with open('index.html', 'w') as f:
	#f.write(response.text)
	#f.write(response.json)

soup = BeautifulSoup(response.text, 'html.parser')
#soup = BeautifulSoup(response.text, 'html5lib')
#soup = BeautifulSoup(response.text, 'lxml-xml')

#print(soup.prettify())

#Func to recursively cross DOM
#def cross_dom(item, level=0)
#	#print item
#	if item.name:
#		print(f"{' ' * level}<{item.name}>")

#	#if item has kids, cross them
#	if hasattr(item, 'children'):
#		for child in item.children:
#			cross_dom(child, level+1)

##start
#cross_dom(soup)

images = soup.find_all('article', class_="product_pod")
pprint(images)
aside = soup.find('aside')
side_categories = aside.find('div', class_='side_categories')
links = side_categories.find_all('a')
pprint(links)
#aside.parent