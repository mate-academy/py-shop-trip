from app.car import Car
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = list(location)

    def ride_to(self, shop: "Shop") -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location

    def ride_home(self, total_cost: float) -> None:
        print(f"{self.name} rides home")
        self.money = round(self.money - total_cost, 2)
        print(f"{self.name} now has {self.money} dollars")
        self.location = self.home_location
