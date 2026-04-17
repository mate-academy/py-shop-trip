import math


class Customer:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.money = float(data["money"])
        self.car = data["car"]

    def get_distance(self, target_location: list[int]) -> float:
        return math.sqrt(
            (self.location[0] - target_location[0]) ** 2
            + (self.location[1] - target_location[1]) ** 2
        )

    def calculate_trip_cost(self, shop: any, fuel_price: float) -> float:
        distance = self.get_distance(shop.location)
        # Ida y vuelta
        fuel_needed = (distance * 2 * self.car["fuel_consumption"]) / 100
        fuel_cost = fuel_needed * fuel_price

        product_cost = 0.0
        for item, quantity in self.product_cart.items():
            product_cost += quantity * shop.products[item]

        return fuel_cost + product_cost
