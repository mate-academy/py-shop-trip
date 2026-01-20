from math import dist
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def count_money(self) -> str:
        return f"{self.name} has {self.money} dollars"

    def distance(self, shop: Shop) -> float:
        return dist(shop.location, self.location)

    def fare(self, shop: Shop, fuel_price: float) -> float:
        return 2 * (self.distance(shop) * self.car.cost_per_km() * fuel_price)

    def product_cost(self, shop: Shop) -> dict:
        return {
            shop.name: {
                key: (value * self.product_cart[key])
                for key, value in shop.products.items()
            }
        }

    def product_price(self, shop: Shop) -> dict:
        return {
            shop: sum(products.values())
            for shop, products in self.product_cost(shop).items()
        }

    def total_cost(self, shops: list, fuel_price: float) -> dict:
        dict_cost_trip = {}

        for shop in shops:
            product = self.product_price(shop)[shop.name]
            fuel = self.fare(shop, fuel_price)
            cost_trip = {
                shop.name: round(product + fuel, 2)
            }
            dict_cost_trip.update(cost_trip)
        return dict_cost_trip

    def min_total_cost(self, shops: list, fuel_price: float) -> str:

        min_cost_trip = min(self.total_cost(shops, fuel_price).values())
        for key, value in self.total_cost(shops, fuel_price).items():
            if value != min_cost_trip:
                continue
            return key

    def money_remains(
            self,
            shops: list[Shop],
            fuel_price: float,
            min_trip: str
    ) -> int:
        return self.money - self.total_cost(shops, fuel_price)[min_trip]
