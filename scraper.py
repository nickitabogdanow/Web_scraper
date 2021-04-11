import requests
import string
import os

from bs4 import BeautifulSoup

N = int(input())
typy_of_articles = input()
n = 1


def remove_punctuation(value):
    value = value.strip()
    for c in value:
        if c in string.punctuation:  # or c in ['’', '‘', '—']:
            value = value.replace(c, '')
    value = value.replace(' ', '_')
    return value


def get_request(url):
    r = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(r.content, 'html.parser')
    articles = soup.find_all('article', {'class': 'u-full-height c-card c-card--flush'})
    os.mkdir(f'C:\\Web Scraper\\Web Scraper\\task\\Page_{n}')
    for article in articles:
        type_article = article.find('span', class_='c-meta__type')
        if type_article.text == typy_of_articles:
            find_link = article.find('a', {'data-track-action': 'view article'})
            tail = find_link.get('href')
            url_2 = 'https://www.nature.com' + tail
            r_sub = requests.get(url_2, headers={'Accept-Language': 'en-US,en;q=0.5'})
            soup_2 = BeautifulSoup(r_sub.content, 'html.parser')
            title = soup_2.find('h1', {'class': 'article-item__title'})
            body = soup_2.find('div', class_="article-item__body").text.strip()
            body_byte = body.encode('utf-8')
            title = remove_punctuation(title.text)
            os.chdir(f'C:\\Web Scraper\\Web Scraper\\task\\Page_{n}')
            write_file(title, body_byte)



def write_file(name, content):
    with open(name + '.txt', 'wb') as file:
        file.write(content)


def main():
    global n
    for i in range(N):
        url = f'https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&page={i + 1}'
        get_request(url)
        n += 1


main()
os.chdir(f'C:\\Web Scraper\\Web Scraper\\task')
