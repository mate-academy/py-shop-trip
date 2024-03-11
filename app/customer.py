from typing import Dict, Tuple, List
import datetime
from .shop import Shop
from .utilities import calculate_distance
from .config import config


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: Dict[str, int],
            location: Tuple[float, float],
            money: int,
            car: str
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.original_location = list(location)
        self.money = money
        self.car = car

    def calculate_trip_cost(
            self,
            shop: Shop
    ) -> float:
        distance_to_shop = calculate_distance(self.location, shop.location) * 2
        fuel_cost = (
            self.car.calculate_fuel_cost
            (distance_to_shop, config["FUEL_PRICE"])
        )
        products_cost = (
            sum(shop.products[product] * quantity
                for product, quantity in self.product_cart.items())
        )
        return round(fuel_cost + products_cost, 2)

    def choose_shop(
            self,
            shops: List[Shop]
    ) -> Tuple[Shop, float]:
        cheapest_cost = float("inf")
        cheapest_shop = None
        for shop in shops:
            trip_cost = self.calculate_trip_cost(shop)
            if trip_cost < cheapest_cost and trip_cost <= self.money:
                cheapest_cost = trip_cost
                cheapest_shop = shop
        return cheapest_shop, cheapest_cost

    def make_purchase(
            self,
            shop: Shop,
            datetime_now: datetime.datetime
    ) -> None:
        trip_cost = self.calculate_trip_cost(shop)
        products_cost = (
            sum(shop.products[product] * quantity for product,
                quantity in self.product_cart.items())
        )

        if self.money >= trip_cost:
            self.money -= trip_cost
            self.location = shop.location

            shop.generate_receipt(self, datetime_now, products_cost)
        else:
            print(
                f"{self.name} doesn't have enough money"
                f" to make a purchase in any shop")
