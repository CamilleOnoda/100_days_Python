from math import e
from bs4 import BeautifulSoup
import codecs


with codecs.open("website.html", encoding='cp932', errors='replace') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, ('html.parser'))
print(soup.prettify())

anchor_tags = soup.find_all(name='a')
print(anchor_tags)
for tag in anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.getText())
print()

company_url = soup.select_one(selector="p a")
print(company_url)
print(company_url.getText())