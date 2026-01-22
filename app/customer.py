import math

from app.car import Car
from app.constants import (
    FUEL_CONSUMPTION_PER_100KM,
    TRIP_DIRECTION_MULTIPLIER,
)
from app.shop import Shop
from app.types.types import CarData


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: tuple[int, int],
        money: float,
        car: CarData,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.start_location = location
        self.money = money
        self.car = Car(**car)

    def count_cash(self) -> float:
        return round(self.money, 2)

    def pay(self, amount: float) -> None:
        self.money = round(self.money - amount, 2)

    def has_all_products(self, shop: Shop) -> bool:
        return set(self.product_cart).issubset(shop.products)

    def calculate_distance_to(self, shop: Shop) -> float:
        x1, y1 = self.location
        x2, y2 = shop.location
        return math.hypot(x2 - x1, y2 - y1)

    def calculate_fuel_cost_to(
        self,
        shop: Shop,
        fuel_price: float,
    ) -> float:
        distance = self.calculate_distance_to(shop)
        fuel_used = (
            distance * self.car.fuel_consumption
        ) / FUEL_CONSUMPTION_PER_100KM
        return fuel_used * fuel_price

    def calculate_products_cost(self, shop: Shop) -> float:
        return sum(
            shop.products[product] * quantity
            for product, quantity in self.product_cart.items()
        )

    def calculate_trip_cost(
        self,
        shop: Shop,
        fuel_price: float,
    ) -> float:
        if not self.has_all_products(shop):
            return float("inf")

        fuel_cost = self.calculate_fuel_cost_to(shop, fuel_price)
        total_fuel_cost = fuel_cost * TRIP_DIRECTION_MULTIPLIER
        products_cost = self.calculate_products_cost(shop)

        return round(total_fuel_cost + products_cost, 2)

    def calculate_trip_costs(
        self,
        shops: list[Shop],
        fuel_price: float,
    ) -> list[tuple[Shop, float]]:
        return [
            (shop, self.calculate_trip_cost(shop, fuel_price))
            for shop in shops
        ]

    def find_affordable_shops(
        self,
        trip_costs: list[tuple[Shop, float]],
    ) -> list[tuple[Shop, float]]:
        return [
            (shop, cost)
            for shop, cost in trip_costs
            if cost <= self.money
        ]

    def choose_best_shop(
        self,
        affordable_shops: list[tuple[Shop, float]],
    ) -> tuple[Shop, float]:
        return min(
            affordable_shops,
            key=lambda shop_with_cost: shop_with_cost[1],
        )

    def travel_to(self, destination: tuple[int, int]) -> None:
        self.location = destination

    def visit_shop(self, shop: Shop, total_cost: float) -> None:
        self.pay(total_cost)
        shop.handle_purchase(self)
