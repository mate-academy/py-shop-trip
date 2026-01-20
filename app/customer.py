from math import dist
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_list: dict,
        location: list[int, int],
        money: int,
        car: Car,
    ) -> None:
        self.name = name
        self.product_list = product_list
        self.location = location
        self.money = money
        self.car = car

    def distance_to_shop(self, shop: Shop) -> float:
        return dist(self.location, shop.location)

    def make_purchase(self, shop: Shop) -> float:
        bill = sum(
            self.product_list[product] * shop.products[product]
            for product in self.product_list
        )
        return bill

    def money_to_reach_shop(self, shop: Shop, fuel_price: float) -> float:
        dist = (
            self.distance_to_shop(shop) * fuel_price
            * self.car.fuel_consumption / 100
        )
        dist *= 2
        return round(dist, 2)
