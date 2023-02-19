import requests
import itertools
import os
from twilio.rest import Client

STOCK = "IBIO"  # We can find the equity/company stock code in https://www.tradingview.com/
COMPANY_NAME = "iBio Inc"


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def check_stocks_fluctuation():
    stock_api_key = os.environ['STOCKS_API_KEY']
    stock_api_endpoint = 'https://www.alphavantage.co/query'
    params = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': STOCK,
        'apikey': stock_api_key
    }

    response = requests.get(stock_api_endpoint, params=params)
    response.raise_for_status()
    daily_stocks_data = response.json()['Time Series (Daily)']  # Nested dict

    # We're slicing down the daily stocks data down to the two most recent days.
    sliced_data = dict(itertools.islice(daily_stocks_data.items(), 2))

    close_price_history = [float(sliced_data[day]['4. close']) for day in sliced_data]
    yesterday_closing_price = close_price_history[0]
    day_before_yesterday_closing_price = close_price_history[1]

    close_price_difference = yesterday_closing_price - day_before_yesterday_closing_price
    fluctuation = round(close_price_difference * 100 / yesterday_closing_price, 2)

    if fluctuation >= 5 or fluctuation <= -5:
        send_stock_news_sms(fluctuation)


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
def get_news(company_name):
    news_api_key = os.environ['NEWS_API_KEY']
    news_api_endpoint = 'https://newsapi.org/v2/everything'
    params = {
        'apiKey': news_api_key,
        'q': company_name
    }

    response = requests.get(news_api_endpoint, params=params)
    response.raise_for_status()
    news_data = response.json()['articles'][:3]  # List of dictionaries

    return news_data


# STEP 3: Use https://www.twilio.com
# Send a separate message with the percentage change and each article's title and description to your phone number.
def send_stock_news_sms(fluctuation):

    twilio_account_sid = os.environ['TWILIO_ACCOUNT_SID']
    twilio_auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(twilio_account_sid, twilio_auth_token)

    news_list = get_news(COMPANY_NAME)

    if fluctuation > 0:
        emoji = '🔺'
    else:
        emoji = '🔻'
        fluctuation *= -1

    for article in news_list:
        message = client.messages.create(
            body=f"{STOCK}: {emoji}{fluctuation}%\n"
                 f"Headline: {article['title']}\n"
                 f"Brief: {article['description']}",
            from_=os.environ['TWILIO_VIRTUAL_NUM'],
            to=os.environ['MY_PHONE_NUM']
        )

        print(message.status)


check_stocks_fluctuation()
