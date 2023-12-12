from bs4 import BeautifulSoup
import requests
import lxml
import smtplib


url = "https://www.amazon.co.jp/dp/B09LQVQJF1?ref_=cm_sw_r_apin_dp_A940280NGKEJ6ZZM8CHK&language=ja-JP&fbclid=IwAR1ZsHzKNNZolamYyE85oXsGJSiIfi93yFEkk8QPm_4k0kKs8fgWB2qU0Kg&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7,ja-JP;q=0.6,ja;q=0.5",
}

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.content, 'lxml')
#print(soup.prettify())

price = soup.select_one("span.a-offscreen").getText()
print(price)

price_without_currency = price.strip()
print(ord(price_without_currency[0]))
if ord(price_without_currency[0]) == 65509:
    price_without_currency = price_without_currency[1:]

price_float = float(price_without_currency.replace(',', ''))
print(price_float)

# Email sender
BUY = 20000.0

if price_float < BUY:
    message = f"Shokz OpenRun Pro Earphones now cost {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("email", "password")
        connection.sendmail(
            from_addr="email",
            to_addrs="email",
            msg=f"Amazon Price Alert\n\n{message}\n{url}".encode("utf-8")
        )
