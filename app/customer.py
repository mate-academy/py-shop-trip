from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from app.car import Car
from app.utils import format_amount

if TYPE_CHECKING:
    from app.shop import Shop


@dataclass(slots=True)
class Customer:
    name: str
    product_cart: dict[str, int]
    location: list[int]
    money: float
    car: Car
    home_location: list[int] = field(init=False)

    def __post_init__(self) -> None:
        self.home_location = self.location.copy()

    @classmethod
    def from_dict(cls, customer_data: dict) -> Customer:
        return cls(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            Car(
                customer_data["car"]["brand"],
                customer_data["car"]["fuel_consumption"],
            ),
        )

    def distance_to_shop(self, shop: Shop) -> float:
        return (
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        ) ** 0.5

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        return shop.calculate_products_cost(
            self.product_cart
        ) + 2 * self.car.calculate_fuel_cost(
            self.distance_to_shop(shop), fuel_price
        )

    def get_trip_options(
        self,
        shops: list[Shop],
        fuel_price: float,
    ) -> list[tuple[Shop, float]]:
        return [
            (shop, self.calculate_trip_cost(shop, fuel_price))
            for shop in shops
            if shop.has_products(self.product_cart)
        ]

    def choose_shop(
        self,
        shops: list[Shop],
        fuel_price: float,
    ) -> tuple[Shop, float] | None:
        available_shops = [
            (shop, cost)
            for shop, cost in self.get_trip_options(shops, fuel_price)
            if cost <= self.money
        ]
        if not available_shops:
            return None
        return min(available_shops, key=lambda option: option[1])

    def describe_trip(self, shops: list[Shop], fuel_price: float) -> str:
        options = self.get_trip_options(shops, fuel_price)
        lines = [
            f"{self.name} has {format_amount(self.money)} dollars",
            *(
                f"{self.name}'s trip to the {shop.name} costs {cost:.2f}"
                for shop, cost in options
            ),
        ]

        shop = self.choose_shop(shops, fuel_price)
        if shop is None:
            lines.append(
                f"{self.name} doesn't have enough money "
                "to make a purchase in any shop"
            )
        else:
            lines.append(self.make_trip(*shop))
        return "\n".join(lines)

    def make_trip(self, shop: Shop, trip_cost: float) -> str:
        self.drive_to_shop(shop, trip_cost)
        receipt = shop.create_receipt(self)
        self.drive_home()
        return "\n".join([
            f"{self.name} rides to {shop.name}",
            "",
            receipt,
            "",
            f"{self.name} rides home",
            f"{self.name} now has {self.money:.2f} dollars",
        ])

    def drive_to_shop(self, shop: Shop, trip_cost: float) -> None:
        self.money -= trip_cost
        self.location = shop.location.copy()

    def drive_home(self) -> None:
        self.location = self.home_location.copy()
