from app.car import Car


class Customer:
    def __init__(self, customer_dict: dict, full_price: int) -> None:
        self.full_price = full_price
        self.name = customer_dict["name"]
        self.product_cart = customer_dict["product_cart"]
        self.location = customer_dict["location"]
        self.money = customer_dict["money"]
        self.car = Car(customer_dict["car"])

    def price_100_km(self) -> int:
        return self.full_price * self.car.fuel_consumption
