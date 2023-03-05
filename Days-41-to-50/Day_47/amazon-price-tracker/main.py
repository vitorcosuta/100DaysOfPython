import requests
import os
import smtplib
from bs4 import BeautifulSoup

SMTP_ADDRESS = 'outlook.office365.com'
SENDER_EMAIL = os.environ['SENDER_EMAIL']
RECEIVER_EMAIL = os.environ['RECEIVER_EMAIL']
PASSWORD = os.environ['EMAIL_PASSWORD']
TARGET_PRICE = 10  # Currency: US Dollar


def send_email():
    message = 'Subject:Amazon Price Alert!\n\n'  # Setting the mail subject
    message += f'{product_name} is now {product_price}.\n{product_link}'

    with smtplib.SMTP(SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECEIVER_EMAIL,
            msg=message
        )


product_link = 'https://www.amazon.com/Brave-New-World-Aldous-Huxley/dp/0060850523/ref=sr_1_1?crid=125NNCI2QXKTV'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63',
    'Accept-Language': 'en-US,en;q=0.9,pt;q=0.8,ja;q=0.7'
}

response = requests.get(url=product_link, headers=headers)
response.raise_for_status()
amazon_web_page = response.text
soup = BeautifulSoup(amazon_web_page, 'html.parser')

price_span_tag = soup.select_one('.swatchElement.selected span span span a span span')
product_price = price_span_tag.getText()

# Removing dollar sign
raw_price = float(product_price.split('$')[1])

product_name = soup.find(name='span', id='productTitle').getText()
product_name = product_name.strip()  # Removing white spaces

if raw_price < TARGET_PRICE:
    send_email()
