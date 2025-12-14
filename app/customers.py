from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    @staticmethod
    def distance(ar: list, ba: list) -> float:
        return ((ar[0] - ba[0]) ** 2 + (ar[1] - ba[1]) ** 2) ** 0.5

    def shopping_cost_in(self, shop: Shop) -> float:
        # distance to shop and back
        dist = self.distance(self.location, shop.location)
        fuel_to_shop = self.car.trip_cost(dist)
        fuel_home = self.car.trip_cost(dist)

        # price of products
        product_cost = 0
        for per, amount in self.product_cart.items():
            if per not in shop.products:
                return None
            product_cost += shop.products[per] * amount

        return fuel_to_shop + fuel_home + product_cost
