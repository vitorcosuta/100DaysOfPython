class FlightData:

    def __init__(self, price, departure_airport, departure_city, destination_city, destination_airport, out_date,
                 return_date):
        self.price = price
        self.departure_city = departure_city
        self.departure_airport = departure_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
