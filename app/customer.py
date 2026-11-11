from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.shop import Shop
    from app.car import Car


class Customer:

    def __init__(self, name: str, product_cart: dict,
                 current_location: list[float],
                 money: float, car: Car, home_location: list[float]) -> None:
        self.name = name
        self.product_cart = product_cart
        self.current_location = current_location.copy()
        self.money = money
        self.car = car
        self.home_location = home_location.copy()

    def calculate_trip_cost(self, shop: Shop,
                            fuel_price: float) -> float | None:
        if not shop.check_if_has_products(self.product_cart):
            return None
        distance = self.car.calculate_distance(self.current_location,
                                               shop.location)
        fuel_cost = self.car.fuel_price_per_trip(distance, fuel_price) * 2
        products_cost = shop.calculate_price_of_products(self.product_cart)
        return fuel_cost + products_cost

    def find_cheapest_shop(self, shops: list[Shop],
                           fuel_price: float) -> tuple[Shop, float] | None:
        shop_options = []
        for shop in shops:
            trip_cost = self.calculate_trip_cost(shop, fuel_price)
            if trip_cost is None:
                continue
            print(
                f"{self.name}'s trip to the "
                f"{shop.name} costs {trip_cost:.2f}"
            )
            shop_options.append((shop, trip_cost))
        if not shop_options:
            return None
        cheapest_shop, cheapest_cost = min(
            shop_options,
            key=lambda option: option[1],
        )
        if cheapest_cost > self.money:
            print(
                f"{self.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
            return None
        print(f"{self.name} rides to {cheapest_shop.name}")
        self.current_location = cheapest_shop.location.copy()
        return cheapest_shop, cheapest_cost

    def pay_for_trip(self, trip_cost: float) -> None:
        self.money -= trip_cost

    def go_home(self) -> None:
        self.current_location = self.home_location.copy()
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money:.2f} dollars")
