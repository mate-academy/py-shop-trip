from dataclasses import dataclass
from typing import TYPE_CHECKING
import math


if TYPE_CHECKING:
    from app.car import Car
    from app.shop import Shop


@dataclass
class Customer:
    name: str
    products: dict[str, int]
    location: tuple[int, int]
    money: float
    car: "Car"
    shop: "Shop" = None
    cost: int = 0

    def greet(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calc_trip_to_shop(self, shop: "Shop", fuel_price: float) -> str:
        distance = self.calc_distance(shop)
        fuel_cost = 2 * distance / 100 * self.car.fuel_consumption * fuel_price
        groceries_cost = self.calc_groceries(shop)
        cost = fuel_cost + groceries_cost

        if self.money >= cost:
            if not self.shop:
                self.shop = shop
                self.cost = cost
            elif self.cost > cost:
                self.shop = shop
                self.cost = cost

        print(f"{self.name}\'s trip to the {shop.name} costs {cost:.2f}")

    def calc_distance(self, shop: "Shop") -> float:
        return math.sqrt(
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        )

    def calc_groceries(self, shop: "Shop") -> float:
        return shop.calc_groceries_cost(self)

    def ride_for_shopping(self) -> None:
        if not self.shop:
            print(
                f"{self.name} doesn't have enough money",
                "to make a purchase in any shop",
            )

        else:
            print(f"{self.name} rides to {self.shop.name}\n")
            self.location = self.shop.location
            self.shop.print_recipe(self)
            self.money -= self.cost
            print(f"{self.name} rides home")
            print(f"{self.name} now has {self.money:.2f} dollars\n")
