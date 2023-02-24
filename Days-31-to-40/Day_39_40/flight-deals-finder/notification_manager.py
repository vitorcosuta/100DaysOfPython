from flight_data import FlightData
from twilio.rest import Client
import os

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
MY_PHONE_NUMBER = os.environ['MY_PHONE_NUMBER']
TWILIO_VIRTUAL_NUMBER = os.environ['TWILIO_VIRTUAL_NUMBER']

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