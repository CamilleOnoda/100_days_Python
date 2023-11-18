from math import e
from bs4 import BeautifulSoup
import requests


response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')
articles = soup.select(".titleline a")
article_texts = []
article_links = []
article_votes = []

for tag in articles:
    text = tag.getText()
    link = tag.get("href")
    article_texts.append(text)
    article_links.append(link)

for votes in soup.select('span .score'):
    article_votes.append((int(votes.getText().split()[0])))


print(article_links)
print()
print(article_texts)
print()
print(sorted(article_votes, reverse=True))