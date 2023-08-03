from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

# Load Classes
from user_data import UserData

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = []


# Load Google Sheets Data
def load_flight_data():
    global sheet_data
    sheet_data = data_manager.get_flight_data()

def add_iatacode():
    for data in sheet_data:
        if data['iataCode'] == '':
            data['iataCode'] = flight_search.get_iata_code(data['city'])
            data_manager.edit_iata_code(data['id'], data['iataCode'])


# Search for Flights
def search_flights():
    print("\nCheapest Flights Found")
    # for data in sheet_data:
    #     flight_data = flight_search.get_one_stop_flights(data['iataCode'])
    #
    #     if flight_data:
    #         if flight_data.price < data['lowestPrice']:
    #             notification_manager.send_message(flight_data)
    flight_data = flight_search.get_one_stop_flights(sheet_data[12]['iataCode'])

# Add New User
def add_user():
    first_name = input("What is your First Name?\n")
    last_name = input("What is your Last Name?\n")
    email = input("What is your Email?\n")
    user = UserData(first_name, last_name, email)
    data_manager.add_user(user)


# User interface for sign up
answer = ""
while answer == "":
    answer = input("Welcome to Puayap's Flight Club\n"
                   "We find the best flight deals and email you.\n"
                   "What do you want to do today?\n"
                   "1. Search for Flights\n"
                   "2. Sign up New User\n"
                   "Enter your answer here: ")

    if answer == "1":
        load_flight_data()
        add_iatacode()
        search_flights()
    elif answer == "2":
        add_user()
    else:
        answer = ""
        print()
