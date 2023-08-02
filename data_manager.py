import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheety_put_endpoint = None
        self.sheety_endpoint = 'https://api.sheety.co/c4ee1ee692651edb4c7ee96edf35311b/flightDeals/prices'
        response = requests.get(url=self.sheety_endpoint)
        self.sheet_data = response.json()['prices']

    def edit_iata_code(self, id, data):
        self.sheety_put_endpoint = f"{self.sheety_endpoint}/{id}"
        parameters = {
            "price": {
                "iataCode": data
            }
        }
        response = requests.put(url=self.sheety_put_endpoint, json=parameters)
        print(response.text)