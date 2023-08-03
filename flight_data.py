class FlightData:

    def __init__(self, origin_city, origin_airport, destination_city, destination_airport, depart_date, return_date, price, stop_overs, via_city):
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.depart_date = depart_date
        self.return_date = return_date
        self.price = price
        self.stop_overs = stop_overs
        self.via_city = via_city