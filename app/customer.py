from dataclasses import dataclass
from decimal import Decimal

from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: Decimal
    car: dict

    def __post_init__(self) -> None:
        self.money = Decimal(str(self.money))

    def calc_dist(self, shop: Shop) -> Decimal:
        return Decimal((((shop.location[0] - self.location[0]) ** 2
                         + (shop.location[1] - self.location[1]) ** 2) ** 0.5))

    def calc_trip_cost(self, shop: Shop, fuel_price: Decimal) -> Decimal:
        return (self.calc_dist(shop) * Decimal(self.car["fuel_consumption"])
                / Decimal("100") * fuel_price)
