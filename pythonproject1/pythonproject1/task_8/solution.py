import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = 'https://soware.ru/categories/material-technical-and-logistics-support-management-systems'
res = requests.get(URL)

if not res.ok:
    raise Exception()

soup = bs(res.text, 'html.parser')
links = soup.find_all('a', class_='dEdHg')
result = []
for link in links:
    result.append(link['href'])

# соседний с a элемент small
names = soup.select('a~small')

df = pd.DataFrame([names, result])
# print(result)
df.to_csv('companies.csv')