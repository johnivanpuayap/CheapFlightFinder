from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

# Load Classes
data_manager = DataManager()
flight_search = FlightSearch()

# Load Google Sheets Data
# sheet_data = data_manager.sheet_data
# pprint(sheet_data)
sheet_data = [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 100},
 {'city': 'Berlin', 'iataCode': 'BER', 'id': 3, 'lowestPrice': 42},
 {'city': 'Tokyo', 'iataCode': 'TYO', 'id': 4, 'lowestPrice': 485},
 {'city': 'Sydney', 'iataCode': 'SYD', 'id': 5, 'lowestPrice': 551},
 {'city': 'Istanbul', 'iataCode': 'IST', 'id': 6, 'lowestPrice': 95},
 {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'id': 7, 'lowestPrice': 414},
 {'city': 'New York', 'iataCode': 'NYC', 'id': 8, 'lowestPrice': 240},
 {'city': 'San Francisco', 'iataCode': 'SFO', 'id': 9, 'lowestPrice': 260},
 {'city': 'Cape Town', 'iataCode': 'CPT', 'id': 10, 'lowestPrice': 378}]


# Get and Replace missing iata Code
for data in sheet_data:
    if data['iataCode'] == '':
        data['iataCode'] = flight_search.get_iata_code(data['city'])
        data_manager.edit_iata_code(data['id'], data['iataCode'])

flight_data = []

for data in sheet_data:
    flight_data = flight_search.get_flights(data['iataCode'])


