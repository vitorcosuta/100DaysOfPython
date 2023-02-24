from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

DEPARTURE_CITY = 'LON'

data_manager = DataManager()
sheet_data = data_manager.get_sheet_data()

flight_search = FlightSearch()

notification_manager = NotificationManager()

for row in sheet_data:
    if row['iataCode'] == '':
        city_name = row['city']
        row_id = row['id']
        row['iataCode'] = flight_search.find_iata_code(city_name)
        data_manager.update_data_row(row['id'], row)

tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_cheapest_flight(
        DEPARTURE_CITY,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today
    )

    if flight.price < destination['lowestPrice']:
        notification_manager.send_flight_deal_notification(flight)
        destination['lowestPrice'] = flight.price
        data_manager.update_data_row(destination['id'], destination)
