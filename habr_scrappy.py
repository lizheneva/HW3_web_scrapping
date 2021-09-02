import requests
from bs4 import BeautifulSoup

KEYWORDS = {'Дизайн', 'Фото', 'Web', 'Python', 'Информационная безопасность*', 'Python*'}
URL = 'https://habr.com'
response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()

soup = BeautifulSoup(response.text, features='html.parser')
articles = soup.find_all('article')

for article in articles:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    hubs = {hub.text.strip() for hub in hubs}
    if KEYWORDS & hubs:
        title = article.find('h2')
        date = article.find('span', class_='tm-article-snippet__datetime-published').text
        href = title.find('a').attrs.get('href')
        print(f'Дата:{date}, Название:{title.text}, Ссылка:{URL + href}')


