from dataclasses import dataclass, field
import math

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: Car
    home_location: list = field(init=False)

    def __post_init__(self) -> None:
        self.home_location = list(self.location)

    def calculate_distance(self, target_location: list) -> float:
        return math.dist(self.location, target_location)

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.calculate_distance(shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance, fuel_price) * 2
        product_cost = shop.calculate_price_products(self.product_cart)
        return fuel_cost + product_cost

    def find_cheapest_shop(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> tuple[Shop, float] | None:
        cheapest: tuple[Shop, float] | None = None
        for shop in shops:
            cost = self.calculate_trip_cost(shop, fuel_price)
            print(
                f"{self.name}'s trip to the {shop.name} costs "
                f"{round(cost, 2)}"
            )
            if cheapest is None or cost < cheapest[1]:
                cheapest = (shop, cost)

        return cheapest

    def rides_to(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = list(shop.location)

    def rides_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = self.home_location

    # def buy(self, shop: Shop, fuel_price: float) -> None:
    #     trip_cost = self.calculate_trip_cost(shop, fuel_price)
    #     shop.print_receipt(self.name, self.product_cart)
    #     self.money -= trip_cost

    def do_shopping(self, shops: list[Shop], fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")
        result = self.find_cheapest_shop(shops, fuel_price)

        if result is None:
            return

        cheapest_shop, trip_cost = result

        if self.money < trip_cost:
            print(
                f"{self.name} doesn't have enough money to make "
                f"a purchase in any shop"
            )
            return

        self.rides_to(cheapest_shop)
        self.money -= trip_cost
        cheapest_shop.print_receipt(self.name, self.product_cart)
        self.rides_home()
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")
