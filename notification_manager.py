import os
from twilio.rest import Client
from flight_data import FlightData


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
        self.TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
        self.TWILIO_PHONE_NUMBER = '+14706135180'
        self.MY_PHONE_NUMBER = '+639561886073'
        self.client = Client(self.TWILIO_ACCOUNT_SID, self.TWILIO_AUTH_TOKEN)

    def send_message(self, flight_data: FlightData):

        body = f"Low price alert! Only Php{flight_data.price} to " \
               f"fly from {flight_data.origin_city}-{flight_data.origin_airport} " \
               f"to {flight_data.destination_city}-{flight_data.destination_airport}, " \
               f"from {flight_data.depart_date} to {flight_data.return_date}"

        message = self.client.messages.create(
            body=body,
            from_=self.TWILIO_PHONE_NUMBER,
            to=self.MY_PHONE_NUMBER
        )

        print("Flight within budget, sent an SMS")
