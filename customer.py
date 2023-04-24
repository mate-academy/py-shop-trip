from car import Car


class Customer:
    def __init__(self, customer_info: dict) -> None:
        self.name = customer_info["name"]
        self.prod = customer_info["product_cart"]
        self.location = customer_info["location"]
        self.money = customer_info["money"]
        self.car = Car(customer_info["car"])
