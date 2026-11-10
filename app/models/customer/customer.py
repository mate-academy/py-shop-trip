from dataclasses import dataclass

from app.models.customer.car import Car
from app.models.shop.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict[str, int | float]
    location: list[int]
    money: float
    car: Car

    def get_money_info(self) -> list[str | int | float]:
        return [self.name, self.money]

    def distance_to_shop(self, shop: Shop) -> float:
        x1, y1 = self.location
        x2, y2 = shop.location
        return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    def calculate_shopping_cost(self, shop: Shop) -> float:
        total_price = 0

        for product, quantity in self.product_cart.items():
            price = shop.products.get(product)
            if price is None or price == 0 or quantity == 0:
                continue

            total_price += price * quantity

        return total_price

    @staticmethod
    def calculate_shopping_trip(
            fuel_cost: int | float,
            shopping_cost: int | float
    ) -> int | float:
        return round(fuel_cost + shopping_cost, 2)
