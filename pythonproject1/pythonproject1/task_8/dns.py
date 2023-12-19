# Считываем сайт DNS. Прокси сервер не даст считать данные с помощью request, поэтому
# сохраняем файл html ctrl+U и парсим

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

with open('index.html') as fp:
    soup = bs(fp, 'html.parser')

names = soup.select('a.catalog-product__name')
id_list = soup.select('div.catalog-product')

if not len(names) == len(id_list):
    raise Exception()

result_list = {'link': [], 'name': [], 'id': []}

for name, prod_id in zip(names, id_list):
    result_list['id'].append(prod_id['data-code'])
    result_list['name'].append(name.text)
    result_list['href'].append('http...') + name['href']
