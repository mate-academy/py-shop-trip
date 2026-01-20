from __future__ import annotations
from math import sqrt

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            home_location: list[int],
            money: float | int,
            car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.home_location = home_location
        self.current_location: list[int] = home_location
        self._money = money
        self.car = car

    @classmethod
    def from_dict(cls, customer_dict: dict) -> Customer:
        return cls(
            customer_dict.get("name"),
            customer_dict.get("product_cart"),
            customer_dict.get("location"),
            customer_dict.get("money"),
            Car.from_dict(customer_dict.get("car")),
        )

    @property
    def money(self) -> float:
        return round(self._money, 2)

    @money.setter
    def money(self, value: float) -> None:
        self._money = value

    def purchase_from(self, shop: Shop) -> None:
        money_spent = shop.service(self.name, self.product_cart)
        self.money -= money_spent

    def ride_to(self, shop: Shop, fuel_price: float) -> None:
        self.money -= self._calculate_gas_cost(shop.location, fuel_price)
        print(f"{self.name} rides to {shop.name}\n")
        self.current_location = shop.location
        self.purchase_from(shop)

    def ride_home(self) -> None:
        self.current_location = self.home_location
        print(f"{self.name} rides home")

    def pick_cheapest_shop(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> tuple[Shop, float]:
        trip_prices = {}
        for shop in shops:
            trip_prices[shop] = self._consider_trip(shop, fuel_price)
        cheapest_shop = min(trip_prices, key=trip_prices.get)
        return cheapest_shop, trip_prices[cheapest_shop]

    def _calculate_cart_cost(self, product_prices: dict) -> float:
        return sum(
            count * product_prices[product]
            for product, count in self.product_cart.items()
        )

    def _distance_to(self, other_location: list[int, int]) -> float:
        return sqrt(
            (self.current_location[0] - other_location[0]) ** 2
            + (self.current_location[1] - other_location[1]) ** 2
        )

    def _calculate_gas_cost(
            self,
            other_location: list[int, int],
            fuel_price: float
    ) -> float:
        distance = self._distance_to(other_location) * 2
        return distance * self.car.fuel_consumption * fuel_price / 100

    def _consider_trip(
            self,
            shop: Shop,
            fuel_price: float,
    ) -> float:
        gas_cost = self._calculate_gas_cost(shop.location, fuel_price)
        cart_cost = self._calculate_cart_cost(shop.products)
        total_trip_cost = round(gas_cost + cart_cost, 2)
        print(f"{self.name}'s trip to the {shop.name} costs {total_trip_cost}")
        return total_trip_cost
