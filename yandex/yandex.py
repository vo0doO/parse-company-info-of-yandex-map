from bs4 import BeautifulSoup
import requests


filename = "D:/PYTOHN-PROJECT/yandex_parse/yandex/search_list.html"


def read_file(filename):
	with open(file = filename, mode = "r+b") as f:
		text = f.read()
	return text


def hrefs():
	href_list = []
	category_list = []
	
	text = read_file(filename)
	soup = BeautifulSoup(text, 'lxml')
	items = soup.find_all('a', {'class': 'search-business-snippet-view'})
	for item in items:
		href = item.get('href')
		category = item.find('div', {'class', "search-snippet-categories-view"}).find().text
		category_list.append(category)
		href_list.append(str('http://yandex.ru' + href))
	return href_list, category_list

href, categories = hrefs()
setings = set(categories)
a = "aw"