from bs4 import BeautifulSoup
import requests
import lxml
import smtplib


url = "https://www.amazon.co.jp/%E3%80%90Amazon-co-jp-%E9%99%90%E5%AE%9A%E3%80%91%E3%83%A1%E3%83%AA%E3%83%BC%E3%82%BA%E3%83%91%E3%83%B3%E3%83%84-9-14kg-%E3%81%95%E3%82%89%E3%81%95%E3%82%89%E3%82%A8%E3%82%A2%E3%82%B9%E3%83%AB%E3%83%BC-56%E6%9E%9A%C3%973/dp/B08KQVBD8P/ref=sr_1_4_sspa?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=191C6M7WUWVB0&keywords=diaper%2BL&qid=1700346430&rdc=1&sprefix=diaper%2Bl%2Caps%2C152&sr=8-4-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1&language=en_US&currency=JPY"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
}

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'lxml')
#print(soup.prettify())

price = soup.select_one("span.a-offscreen").getText()
price_without_currency = price.strip('¥')
price_float = float(price_without_currency.replace(',', ''))
print(price_float)

# Email sender
BUY = 6000.0

if price_float < BUY:
    message = f"3 bags of diapers now cost {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("my_email_address", "my_password")
        connection.sendmail(
            from_addr="my_email_address",
            to_addrs="my_email_address",
            msg=f"Amazon Price Alert\n\n{message}\n{url}".encode("utf-8")
        )
