from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.sheet_data
pprint(sheet_data)

for data in sheet_data:
    if data['iataCode'] == '':
        data['iataCode'] = flight_search.get_iata_code(data['city'])
        data_manager.edit_iata_code(data['id'], data['iataCode'])