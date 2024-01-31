from app.car import Car
from app.shop import Shop
import math


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_total_money(self, shop: Shop) -> float:
        distance = self.find_distance_to_shop(shop.location)
        fuel_both_ways = self.calculate_fuel_price(distance)
        spent_product = 0
        for product, count in self.product_cart.items():
            spent_product += count * shop.products[product]

        return round(fuel_both_ways + spent_product, 2)

    def go_to_shop(self, shop: Shop, expected_costs: float) -> None:
        home = self.location
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location
        shop.print_receipt(self.name, self.product_cart)
        self.money -= expected_costs
        self.location = home
        print(f"{self.name} rides home\n"
              f"{self.name} now has {self.money} dollars\n")

    def find_distance_to_shop(self, shop_location: list[int]) -> float:
        return math.dist(shop_location, self.location)
        # return math.sqrt(
        #     ((shop_location[0] - self.location[0]) ** 2)
        #     + ((shop_location[1] - self.location[1]) ** 2)
        # )

    def calculate_fuel_price(self, distance: float) -> float:
        return (
            (self.car.fuel_consumption / 100) * distance * Car.fuel_price * 2
        )
