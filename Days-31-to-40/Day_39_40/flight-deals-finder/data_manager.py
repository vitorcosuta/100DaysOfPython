import requests
import os

ENDPOINT = 'https://api.sheety.co/b70343d18fb5bf9c870e534c1d4bc379/flightDeals/prices'
BEARER_TOKEN = os.environ['SHEETY_BEARER_TOKEN']

headers = {
    'Authorization': BEARER_TOKEN
}


class DataManager:

    def __init__(self):
        response = requests.get(ENDPOINT, headers=headers)
        response.raise_for_status()
        self.data = response.json()['prices']

    def get_sheet_data(self):
        return self.data

    def update_data_row(self, row_id, updated_row):

        for row in self.data:
            if row['id'] == row_id:
                row_index = self.data.index(row)
                self.data[row_index] = updated_row

        query = {
            'price': updated_row
        }

        put_endpoint = ENDPOINT + f'/{row_id}'
        response = requests.put(url=put_endpoint, json=query, headers=headers)
        response.raise_for_status()
