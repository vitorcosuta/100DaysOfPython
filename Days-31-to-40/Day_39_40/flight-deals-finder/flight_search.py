import requests
import os
from flight_data import FlightData

TEQUILA_ENDPOINT = 'https://api.tequila.kiwi.com'

class FlightSearch:

    def __init__(self):
        self.cheapest_flights = []

    def find_iata_code(self, location_name):
        get_endpoint = TEQUILA_ENDPOINT + '/locations/query'
        headers = {'apikey': os.environ['TEQUILA_API_KEY']}

        query = {
            'term': location_name,
            'location_types': 'city'
        }

        response = requests.get(url=get_endpoint, headers=headers, params=query)
        response.raise_for_status()

        iata_code = response.json()['locations'][0]['code']
        return iata_code

    def check_cheapest_flight(self, departure_city_code, destination_city_code, from_time, to_time):
        headers = {'apikey': os.environ['TEQUILA_API_KEY']}

        query = {
            'fly_from': departure_city_code,
            'fly_to': destination_city_code,
            'date_from': from_time.strftime('%d/%m/%Y'),
            'date_to': to_time.strftime('%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': 'round',
            'one_for_city': 1,  # Returns the cheapest flight
            'max_stopovers': 0,  # Direct flights
            'curr': 'USD'
        }

        response = requests.get(url=f'{TEQUILA_ENDPOINT}/v2/search', headers=headers, params=query)

        try:
            data = response.json()['data'][0]
        except IndexError:
            query['max_stopovers'] = 1
            response = requests.get(url=f'{TEQUILA_ENDPOINT}/v2/search', headers=headers, params=query)
            try:
                data = response.json()['data'][0]
            except IndexError:
                # print(f'No flights found for {destination_city_code}')
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    departure_city=data["route"][0]["cityFrom"],
                    departure_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
        else:
            flight_data = FlightData(
                price=data["price"],
                departure_city=data["route"][0]["cityFrom"],
                departure_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )

        # print(f'{flight_data.destination_city} : $ {flight_data.price}')

        return flight_data
