from app.fuel import Fuel


class Car:
    def __init__(self, params):
        self.brand = params["brand"]
        self.fuel_consumption = params["fuel_consumption"]

    def trip_price(self, distance):
        result = 2 * distance * self.fuel_consumption * Fuel.FUEL_PRICE / 100
        return round(result, 2)

    def make_trip_to(self, customer, location):
        customer.location = location
