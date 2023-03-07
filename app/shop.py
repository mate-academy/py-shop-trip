from math import dist


class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def calc_prod_price(self, customer_cart: dict) -> float:
        total = 0
        for item, count in customer_cart.items():
            total += self.products[item] * count
        return total

    def calc_distance(self, customer_location: list) -> float:
        return dist(self.location, customer_location)
