# This code is not going to work because some confidential data has been omitted from the code.

import requests
from twilio.rest import Client

OPW_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
api_key = 'xxx'
latitude = -19.917299
longitude = -43.934559
account_sid = 'xxx'
auth_token = 'xxx'

params = {
    'lat': latitude,
    'lon': longitude,
    'appid': api_key,
    'units': 'metric'
}


def forecast_rain():
    """Forecasts if it's going to rain in the next 12 hours"""

    response = requests.get(OPW_ENDPOINT, params=params)
    response.raise_for_status()
    weather_data = response.json()
    # Taking the next 12 hours (each index in the list refers to a 3-hour interval, so we need to slice the list down to
    # the first 4 indexes).
    weather_slice = weather_data['list'][:4]

    for hour_interval in weather_slice:
        interval_weather_details = hour_interval['weather']  # List with dicts each containing the weather details

        for weather_element in interval_weather_details:
            if weather_element['id'] < 700:
                send_SMS_rain_alert()
                return


def send_SMS_rain_alert():

    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella. ☔",
        from_='+111',
        to='Your phone number'
    )

    print(message.status)


forecast_rain()
