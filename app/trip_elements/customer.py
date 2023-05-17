from app.trip_elements.car import Car


class Customer:
    def __init__(self, customer: dict):
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.home_location = customer["location"]
        self.money = customer["money"]
        self.car = Car(customer["car"])
