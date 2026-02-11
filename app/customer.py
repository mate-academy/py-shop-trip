from __future__ import annotations
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.car import Car
    from app.shop import Shop


@dataclass
class Customer:
    name: str
    products_to_buy: dict[str, int]
    location: tuple[int, int]
    money: float
    car: Car
    where_to_go: list[tuple[Shop, float]] = field(default_factory=list)

    def calculate_trip(self, shop: Shop) -> str:
        shop_travel_price = (
            self.car.trip_fuel_consumption(self.location, shop.location)
        )
        total_product_price = 0
        for product, price in shop.products.items():
            one_product_price = self.products_to_buy[product] * price
            total_product_price += one_product_price
        trip_price = (round(total_product_price, 2)
                      + round(shop_travel_price, 2))
        self.where_to_go.append((shop, trip_price))

        return f"{self.name}'s trip to the {shop.name} costs {trip_price:.2f}"
