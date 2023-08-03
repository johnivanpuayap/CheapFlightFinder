import requests
from user_data import UserData


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.prices_endpoint = 'https://api.sheety.co/c4ee1ee692651edb4c7ee96edf35311b/flightDeals/prices'
        self.users_post_endpoint = f"https://api.sheety.co/c4ee1ee692651edb4c7ee96edf35311b/flightDeals/users"

    def get_flight_data(self):

        # response = requests.get(url=self.prices_endpoint)
        # sheet_data = response.json()['prices']
        # This is to limit the number of calls to Sheety API since it is very limited
        sheet_data = [
            {'city': 'Manila', 'iataCode': 'MNL', 'id': 2, 'lowestPrice': 1000},
            {'city': 'Bangkok', 'iataCode': 'BKK', 'id': 3, 'lowestPrice': 8000},
            {'city': 'Singapore', 'iataCode': 'SIN', 'id': 4, 'lowestPrice': 12000},
            {'city': 'Seoul', 'iataCode': 'ICN', 'id': 5, 'lowestPrice': 7000},
            {'city': 'Beijing', 'iataCode': 'PEK', 'id': 6, 'lowestPrice': 5000},
            {'city': 'Shanghai', 'iataCode': 'PVG', 'id': 7, 'lowestPrice': 5600},
            {'city': 'Jakarta', 'iataCode': 'CGK', 'id': 8, 'lowestPrice': 9000},
            {'city': 'Ho Chi Minh City', 'iataCode': 'SGN', 'id': 9, 'lowestPrice': 6000},
            {'city': 'Hong Kong', 'iataCode': 'HKG', 'id': 10, 'lowestPrice': 6400},
            {'city': 'Taipei', 'iataCode': 'TPE', 'id': 11, 'lowestPrice': 8400},
            {'city': 'Bali', 'iataCode': 'DPS', 'id': 12, 'lowestPrice': 12000}]
        return sheet_data

    def edit_iata_code(self, id, data):
        prices_put_endpoint = f"{self.prices_endpoint}/{id}"
        parameters = {
            "price": {
                "iataCode": data
            }
        }
        response = requests.put(url=prices_put_endpoint, json=parameters)
        print(response.text)

    def add_user(self, user: UserData):
        parameters = {
            "user": {
                "firstName": user.first_name,
                "lastName": user.last_name,
                "email": user.email,
                "phoneNumber": user.phone_number,
            }
        }
        response = requests.post(url=self.users_post_endpoint, json=parameters)
        print(response.status_code)
        print(response.text)
