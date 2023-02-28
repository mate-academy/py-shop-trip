class Car:
    def __init__(self, car_info):
        self.brand = car_info["brand"]
        self.fuel_consumption = car_info["fuel_consumption"]

    def trip_price(self, fuel_price, distance):
        return round((fuel_price * distance * self.fuel_consumption / 100) * 2, 2)

    @staticmethod
    def ride_home(customer):
        print(f"{customer.name} rides home")
