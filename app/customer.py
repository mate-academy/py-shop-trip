import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            location: list,
            money: int | float,
            product_cart: dict,
            car: Car
    ) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.product_cart = product_cart
        self.car = car

    def distance_to(self, shop_location: list) -> float:
        return math.hypot(self.location[0] - shop_location[0],
                          self.location[1] - shop_location[1])

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.distance_to(shop.location)
        fuel_expense = self.car.fuel_cost(distance * 2, fuel_price)

        products_cost = 0
        for product, quantity in self.product_cart.items():
            if product not in shop.products:
                return float("inf")
            products_cost += shop.products[product] * quantity

        return fuel_expense + products_cost

    def go_to_shop(
            self,
            shop: Shop,
            fuel_price: float,
            trip_cost: float
    ) -> None:
        print(f"{self.name} rides to {shop.name}")
        home_location = self.location.copy()
        self.location = shop.location.copy()

        shop.print_receipt(self.name, self.product_cart)

        self.money -= trip_cost
        print(f"{self.name} rides home")
        self.location = home_location
        print(f"{self.name} now has {self.money:.2f} dollars")  # noqa: E231
