from app.car import Car


class Customer:

    customers = []

    def __init__(self, customer: dict) -> None:
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
        Customer.customers.append(self)
