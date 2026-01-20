from math import sqrt

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str, products: dict,
                 location: list, money: int, car: Car) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance(self, shop: list) -> float:
        return sqrt((self.location[0] - shop[0]) ** 2
                    + (self.location[1] - shop[1]) ** 2)

    def calculate_trip_cost(self, shop: Shop,
                            fuel_price: float) -> tuple:
        distance_to_shop = self.calculate_distance(shop.location)
        fuel_cost_to_shop = self.car.calculate_fuel_cost(distance_to_shop,
                                                         fuel_price)
        fuel_cost_return = fuel_cost_to_shop
        total_fuel_cost = fuel_cost_to_shop + fuel_cost_return

        product_cost = sum(
            shop.products.get(product) * quantity
            for product, quantity in self.products.items()
        )

        return product_cost + total_fuel_cost, total_fuel_cost

    def buy_products(self, shop: Shop) -> None:
        total_cost = 0
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        for product, quantity in self.products.items():
            price = shop.products[product]
            product_cost = price * quantity
            if ("." in str(product_cost)
                    and str(product_cost).split(".")[1] == "0"):
                print(f"{quantity} {product}{'s' if quantity > 1 else ''} "
                      f"for {int(product_cost)} dollars")
            else:
                print(f"{quantity} {product}{'s' if quantity > 1 else ''} "
                      f"for {product_cost} dollars")
            total_cost += product_cost

        print(f"Total cost is {total_cost} dollars\nSee you again!")
        self.money -= total_cost
