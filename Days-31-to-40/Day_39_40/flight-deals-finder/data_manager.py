import requests
import os

PRICES_ENDPOINT = 'https://api.sheety.co/b70343d18fb5bf9c870e534c1d4bc379/flightDeals/prices'
USERS_ENDPOINT = 'https://api.sheety.co/b70343d18fb5bf9c870e534c1d4bc379/flightDeals/users'
BEARER_TOKEN = os.environ['SHEETY_BEARER_TOKEN']

headers = {
    'Authorization': BEARER_TOKEN
}


class DataManager:

    def __init__(self):
        response = requests.get(PRICES_ENDPOINT, headers=headers)
        response.raise_for_status()
        self.prices_data = response.json()['prices']

        response = requests.get(USERS_ENDPOINT, headers=headers)
        response.raise_for_status()
        self.users_data = response.json()['users']

    def get_price_sheet_data(self):
        return self.prices_data

    def get_user_sheet_data(self):
        return self.users_data

    def update_data_row(self, row_id, updated_row):

        for row in self.prices_data:
            if row['id'] == row_id:
                row_index = self.prices_data.index(row)
                self.prices_data[row_index] = updated_row

        query = {
            'price': updated_row
        }

        put_endpoint = PRICES_ENDPOINT + f'/{row_id}'
        response = requests.put(url=put_endpoint, json=query, headers=headers)
        response.raise_for_status()

    def add_user(self, first_name, last_name, email):

        body = {
            'user': {
                'firstName': first_name,
                'lastName': last_name,
                'email': email
            }
        }

        response = requests.post(url=USERS_ENDPOINT, json=body, headers=headers)
        response.raise_for_status()

        if response.status_code == requests.codes.ok:
            print("You're in the club!")
        else:
            print('Something went wrong.')
