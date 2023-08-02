import os

import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_search_endpoint = 'https://api.tequila.kiwi.com'
        self.flight_search_api_key = '5DyoV7Vy4vpc1udpKm2RliiCFmiUOh81'

    def get_iata_code(self, city):
        flight_search_endpoint_locations = f"{self.flight_search_endpoint}/locations/query"
        headers = {
            "apikey": self.flight_search_api_key
        }
        parameters = {
            "term": city,
        }

        response = requests.get(url=flight_search_endpoint_locations, params=parameters, headers=headers)
        location_data = response.json()
        iata_code = location_data['locations'][0]['code']

        return iata_code
