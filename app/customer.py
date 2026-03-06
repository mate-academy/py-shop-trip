import math


class Customer:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.brand = data["car"]["brand"]
        self.fuel_consumption = data["car"]["fuel_consumption"]

    def get_fuel_cost(self, shop_location: list, fuel_price: float) -> float:
        dist = math.sqrt(pow(shop_location[0] - self.location[0], 2)
                         + pow(shop_location[1] - self.location[1], 2))
        fuel_cost = (2 * dist * self.fuel_consumption) / 100 * fuel_price
        return fuel_cost
