from app.car import Car


class Customer:
    def __init__(self, info_dict: dict) -> None:
        self.name = info_dict["name"]
        self.location = info_dict["location"]
        self.money = info_dict["money"]
        self.product_cart = info_dict["product_cart"]
        self.car = Car(info_dict["car"])
