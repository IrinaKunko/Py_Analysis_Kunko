import requests
import BeautifulsSoup4

# объект ответа
response = requests.get('https://roadmap.sh/python')

# Выводим статус ответа
print(response.status_code)
# Успешен или не успешен запрос
print(response.ok)
# выводим ответ на экран
print(response.text)

