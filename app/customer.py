from app.car import Car


class Customer:
    def __init__(self, customer_data: dict) -> None:
        self.name = customer_data["name"]
        self.product_cart = customer_data["product_cart"]
        self.location = customer_data["location"]
        self.money = customer_data["money"]
        self.car = Car(customer_data["car"])
