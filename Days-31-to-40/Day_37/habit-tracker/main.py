import requests
import os
from datetime import datetime

USERNAME = 'vitorcosta'
AUTH_TOKEN = os.environ['AUTH_TOKEN']

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': AUTH_TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# Creating our user in Pixela
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_id = 'graph1'

graph_config = {
    'id': graph_id,
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'momiji'
}

headers = {
    'X-USER-TOKEN': AUTH_TOKEN
}

# Starting a new graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f'{graph_endpoint}/{graph_id}'

today = datetime.now()
yesterday = datetime(year=2023, month=2, day=19)  # We can create dates with datetime like this

add_pixel_config = {
    # Docs for datetime.strftime() method: https://www.w3schools.com/python/python_datetime.asp
    'date': today.strftime("%Y%m%d"),
    'quantity': '15'
}

# Creating new pixel on graph
# response = requests.post(url=pixel_endpoint, json=add_pixel_config, headers=headers)
# print(response)

update_pixel_endpoint = f'{pixel_endpoint}/{yesterday.strftime("%Y%m%d")}'

update_pixel_config = {
    'quantity': '11.5'
}

# Updating a pixel on the graph
# response = requests.put(url=update_pixel_endpoint, json=update_pixel_config, headers=headers)
# print(response.text)

delete_pixel_endpoint = f'{pixel_endpoint}/{yesterday.strftime("%Y%m%d")}'

# Deleting a pixel from the graph
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
