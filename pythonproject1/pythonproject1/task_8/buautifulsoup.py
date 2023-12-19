import requests
from bs4 import BeautifulSoup as bs

URL_TEMPLATE = 'https://soware.ru/categories/clients-and-partners-search-services'
r = requests.get(URL_TEMPLATE)

soup = bs(r.text, 'html.parser')
a_tags = soup.find_all('a', 'dEWdHg')
h1_tag = soup.find('h1')

print(len(a_tags))
print(h1_tag.text)
print(type(h1_tag))

URL = 'https://soware.ru'
res = requests.get(URL)
if not res.ok:
    raise Exception()

soup = bs(res.text, 'html.parser')
soup.fin_all('div')
# Возвращает объект beautiful, расположение объекта в html, содержание этого объекта
soup.find('div', {'class': 'class_name', 'id': 'name_id'})

soup.find('div')
soup.find('qwertio')

soup.select('div')
soup.select('div')

# По классу
soup.select('div.class_name')
soup.select('.class_name')

# По id
soup.select('div#id_name')
soup.select('#id_name')

# По атрибуту
soup.select('[href]')
soup.select('[href="http://..."]')

# Комбинаторы
# \Комбинатор потомков
soup.select('div a')
soup.select('div div p')

# Комбинатор дочерних элементов
soup.select('div > a')
soup.select('div > div > h1')

# Комбинатоор одноуровневых соседей
soup.select('h1 + span')

# Обращение к элементу
h1 = soup.h1
h1_ = soup.h1.a
p = soup.div.p[0]