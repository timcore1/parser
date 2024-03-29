# Для начала вам потребуется установить необходимые библиотеки (если они еще не установлены):

pip install requests beautifulsoup4

# Теперь можно написать код парсера:

import requests
from bs4 import BeautifulSoup
# URL сайта, который хотим спарсить
url = "http://example.com/"
# Совершаем HTTP-GET запрос к сайту
response = requests.get(url)
# Проверяем статус ответа
if response.status_code == 200:
    # Используем BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Ищем интересующие нас элементы на странице. Например, предположим, что статьи
    # находятся в элементах с классом "article-title" и они представлены в виде ссылок
    articles = soup.find_all('a', class_='article-title')
    
    # Извлекаем название и URL каждой статьи
    for article in articles:
        title = article.text.strip()  # получаем текст ссылки
        link = article.get('href')    # получаем атрибут href (URL)
        print(f"Article Title: {title}, Article URL: {link}")
else:
    print("Failed to retrieve the webpage")
