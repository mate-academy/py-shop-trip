from __future__ import annotations

from app.car import Car
from app.point import Point
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: Point,
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart or {}
        self.location = location
        self.money = money
        self.car = car

    @classmethod
    def create_customer(
            cls,
            source: dict[str, str | dict[str, int] | list[int] | int]
    ) -> Customer:
        return cls(
            source["name"],
            source["product_cart"],
            Point.create_from_location(source["location"]),
            source["money"],
            Car.create_car(source["car"])
        )

    def choose_shop(self, shops: list) -> Shop | None:
        for shop in shops:
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {self._calculate_total_expenses(shop)}")

        cheapest_shop = min(
            shops,
            key=lambda shop: self._calculate_total_expenses(shop)
        )
        total_expenses = self._calculate_total_expenses(cheapest_shop)
        if self.money < total_expenses:
            return None
        self.money -= total_expenses
        return cheapest_shop

    def _calculate_total_expenses(self, shop: Shop) -> float:
        distance = self.location.calculate_distance_to(shop.location)
        fuel_expenses = (
            (self.car.calculate_fuel_consumption(distance) * 2) * 2.4
        )
        groceries_expenses = (
            self._calculate_groceries_expenses(shop.products)
        )

        return round(fuel_expenses + groceries_expenses, 2)

    def _calculate_groceries_expenses(self, prices: dict) -> float:
        return sum(
            prices[product_name] * amount
            for product_name, amount in self.product_cart.items()
        )
