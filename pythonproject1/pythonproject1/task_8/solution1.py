import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL = 'https://soware.ru/categories/reference'
res = requests.get(URL)

if not res.ok:
    raise Exception()

soup = bs(res.text, 'html.parser')
links = soup.select('html.parser')
result = {'link': [], 'ref': []}

for link in links:
    result['link'].append('https://soware.ru'+link['href'])
    result['ref'].append(link.text)

df = pd.DataFrame(result)
# print(result)
df.to_csv('companies.csv')