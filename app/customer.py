import math

from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: list[int],
            money: float | int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance(
            self,
            shop_location: list[int]
    ) -> float | int:
        x1, y1 = self.location
        x2, y2 = shop_location
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) * 2

    def purchases_cost(self, products: dict[str, int]) -> float | int:
        costs = 0
        for product in self.product_cart:
            costs += self.product_cart[product] * products[product]

        return costs

    def go_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars")
        print()

    def go_buy(self, shop_name: str, costs_amount: float | int) -> None:
        self.money -= costs_amount
        print(f"{self.name} rides to {shop_name}")
        print()

    def go_shop(self, shop_name: str, total_costs: float | int) -> None:
        print(
            f"{self.name}'s trip to the "
            f"{shop_name} costs {total_costs}"
        )

    def has_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")
