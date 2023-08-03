import requests
from user_data import UserData


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.prices_endpoint = 'https://api.sheety.co/c4ee1ee692651edb4c7ee96edf35311b/flightDeals/prices'
        self.users_post_endpoint = f"https://api.sheety.co/c4ee1ee692651edb4c7ee96edf35311b/flightDeals/users"

    def get_flight_data(self):
        response = requests.get(url=self.prices_endpoint)
        sheet_data = response.json()['prices']
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
