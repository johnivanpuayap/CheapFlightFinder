import os
from pprint import pprint

import requests
from datetime import datetime, timedelta
from flight_data import FlightData

STARTING_CITY = 'LON'


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.starting_city = STARTING_CITY
        self.curr = 'PHP'
        self.flight_search_endpoint_search = f"https://api.tequila.kiwi.com/v2/search"
        self.flight_search_endpoint_locations = f"https://api.tequila.kiwi.com/locations/query"
        self.headers = {
            "apikey": os.environ['FLIGHT_SEARCH_API_KEY']
        }

    def get_flights(self, departure_city_code) -> FlightData:
        date_today = datetime.now()
        tomorrow = (date_today + timedelta(days=1)).strftime("%d/%m/%Y")
        six_months = (date_today + timedelta(days=180)).strftime("%d/%m/%Y")

        parameters = {
            "fly_from": self.starting_city,
            "fly_to": departure_city_code,
            "date_from": tomorrow,
            "date_to": six_months,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": self.curr,
            "one_for_city": 1,
        }

        # response = requests.get(self.flight_search_endpoint_search, params=parameters, headers=self.headers)
        response = []
        try:
            # data = response.json()['data'][0]
            # For testing purposes
            data = response[0]
        except IndexError:
            print(f"No direct flights found to {departure_city_code}")
            parameters["max_stopovers"] = 1
            response = requests.get(self.flight_search_endpoint_search, params=parameters, headers=self.headers)
            try:
                data = response.json()['data'][0]
            except IndexError:
                print(f"No 1 stop flights found to {departure_city_code}")
                return None
            else:
                pprint(parameters)
                pprint(data)
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
                print(f"{flight_data.destination_city}: {flight_data.price} Php")
                print(f"Flight has {flight_data.stop_overs} stop over, via {flight_data.via_city}")
                return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                depart_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][0]["local_departure"].split("T")[0],
                stop_overs=0,
                via_city=""
            )
        print(f"{flight_data.destination_city}: {flight_data.price} Php")
        return flight_data

    def get_iata_code(self, city):
        parameters = {
            "term": city,
        }

        response = requests.get(url=self.flight_search_endpoint_locations, params=parameters, headers=self.headers)
        location_data = response.json()
        iata_code = location_data['locations'][0]['code']

        return iata_code
