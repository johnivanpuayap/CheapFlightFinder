import os

import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.flight_search_endpoint = ''
        self.flight_search_api_key = os.environ['FLIGHT_SEARCH_API_KEY']

    def get_iata_code(self, city):
        return "TESTING"
