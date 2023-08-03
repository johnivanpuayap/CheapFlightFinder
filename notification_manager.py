import os
import smtplib
from twilio.rest import Client
from flight_data import FlightData


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        # TWILIO DATA
        self.TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
        self.TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
        self.TWILIO_PHONE_NUMBER = '+14706135180'
        self.MY_PHONE_NUMBER = '+639561886073'
        self.client = Client(self.TWILIO_ACCOUNT_SID, self.TWILIO_AUTH_TOKEN)

        # EMAIL DATA
        self.EMAIL = 'johnivanpuayapamerica@gmail.com'
        self.EMAIL_PASSWORD = os.environ['EMAIL_PASSWORD']

    def send_message(self, flight_data: FlightData):

        body = f"Low price alert! Only {flight_data.price} Php to " \
               f"fly from {flight_data.origin_city}-{flight_data.origin_airport} " \
               f"to {flight_data.destination_city}-{flight_data.destination_airport}, " \
               f"from {flight_data.depart_date} to {flight_data.return_date}"

        if flight_data.stop_overs == 1:
            body = f"{body}\nFlight has {flight_data.stop_overs} stop over, via {flight_data.via_city}."

        message = self.client.messages.create(
            body=body,
            from_=self.TWILIO_PHONE_NUMBER,
            to=self.MY_PHONE_NUMBER
        )

        print("Flight within budget, sent an SMS")

    def send_emails(self, email, flight_data: FlightData):
        body = f"Subject: Puayap's Flight Club Low Price Alert\n\nLow price alert! Only {flight_data.price} Php to " \
               f"fly from {flight_data.origin_city}-{flight_data.origin_airport} " \
               f"to {flight_data.destination_city}-{flight_data.destination_airport}, " \
               f"from {flight_data.depart_date} to {flight_data.return_date}"

        if flight_data.stop_overs == 1:
            body = f"{body}\nFlight has {flight_data.stop_overs} stop over, via {flight_data.via_city}."

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.EMAIL, password=self.EMAIL_PASSWORD)
            connection.sendmail(from_addr=self.EMAIL, to_addrs=email, msg=body)

