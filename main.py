from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

# Load Classes
data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# Load Google Sheets Data
# sheet_data = data_manager.sheet_data
# pprint(sheet_data)
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
    {'city': 'Taipei', 'iataCode': 'TPE', 'id': 11, 'lowestPrice': 8400}]

# Get and Replace missing iata Code
for data in sheet_data:
    if data['iataCode'] == '':
        data['iataCode'] = flight_search.get_iata_code(data['city'])
        data_manager.edit_iata_code(data['id'], data['iataCode'])

# Search for Flights
for data in sheet_data:
    flight_data = flight_search.get_flights(data['iataCode'])

    if flight_data:
        if flight_data.price < data['lowestPrice']:
            notification_manager.send_message(flight_data)



