import requests
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
import os

DEPARTURE_CITY = 'LON'
BEARER_TOKEN = os.environ['SHEETY_BEARER_TOKEN']


def sign_in():

    print('Welcome to the Flight Club! \n We find the best flight deals and email you.')
    first_name = input('What is your first name? \n')
    last_name = input('What is your last name? \n')
    email = input('What is your email? \n')
    email_verification = input('Type your email again, please. \n')

    while email != email_verification:
        print("Your emails don't match.")
        email = input('What is your email? \n')
        email_verification = input('Type your email again, please. \n')

    data_manager.add_user(first_name, last_name, email)


data_manager = DataManager()
price_sheet_data = data_manager.get_price_sheet_data()
user_sheet_data = data_manager.get_user_sheet_data()

flight_search = FlightSearch()

notification_manager = NotificationManager()

for row in price_sheet_data:
    if row['iataCode'] == '':
        city_name = row['city']
        row_id = row['id']
        row['iataCode'] = flight_search.find_iata_code(city_name)
        data_manager.update_data_row(row['id'], row)

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in price_sheet_data:
    flight = flight_search.check_cheapest_flight(
        DEPARTURE_CITY,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    if flight is not None:
        if flight.price < destination['lowestPrice']:
            notification_manager.send_flight_deal_notification(flight)
            destination['lowestPrice'] = flight.price
            data_manager.update_data_row(destination['id'], destination)

            for user in user_sheet_data:
                notification_manager.send_flight_deal_email(flight, user['email'])

# sign_in()
