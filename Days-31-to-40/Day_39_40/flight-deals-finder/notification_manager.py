from flight_data import FlightData
from twilio.rest import Client
import smtplib
import os

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
MY_PHONE_NUMBER = os.environ['MY_PHONE_NUMBER']
TWILIO_VIRTUAL_NUMBER = os.environ['TWILIO_VIRTUAL_NUMBER']
SMTP_ADDRESS = 'outlook.office365.com'
SENDER_EMAIL = os.environ['SENDER_EMAIL']
PASSWORD = os.environ['EMAIL_PASSWORD']

class NotificationManager:

    def send_flight_deal_notification(self, flight: FlightData):

        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages.create(
            body=f'Low price alert! Only ${flight.price} to fly from {flight.departure_city}-{flight.departure_airport}'
                 f'to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} '
                 f'to {flight.return_date}',
            from_=TWILIO_VIRTUAL_NUMBER,
            to=MY_PHONE_NUMBER
        )

        print(message.status)

    def send_flight_deal_email(self, flight: FlightData, user_email):
        msg_text = f'Subject:New Low Price Flight\n\nLow price alert! Only ${flight.price} to fly from' \
              f' {flight.departure_city}-{flight.departure_airport} to {flight.destination_city}-' \
              f'{flight.destination_airport}, from {flight.out_date} to {flight.return_date}'

        if flight.stop_overs > 0:
            msg_text += f'\n\nFlight has {flight.stop_overs} stopovers, via {flight.via_city}'

        link = f'https://www.google.co.uk/flights?hl=en#flt={flight.departure_airport}.{flight.destination_airport}.' \
               f'{flight.out_date}*{flight.destination_airport}.{flight.departure_airport}.{flight.return_date}'

        with smtplib.SMTP(SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(user=SENDER_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=SENDER_EMAIL,
                to_addrs=user_email,
                msg=f'{msg_text}\n{link}'
            )
