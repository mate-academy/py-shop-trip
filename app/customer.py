from car import Car
from math import sqrt


class Customer:
    def __init__(
            self, name: str, product_cart: str, location: str, money: int, car: str, home_location=None
    ):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car
        self.home_location = home_location if home_location else location

    def distance_to(self, other_location):
        return sqrt((self.location[0] - other_location[0])**2 + (self.location[1] - other_location[1])**2)

    def calculate_product_cost(self, shop):
        cost = 0
        for product, quantity in self.product_cart.items():
            cost += shop.products[product] * quantity
        return cost

    def go_to_shop(self, shop, cost):
        self.location = shop.location
        self.money -= cost

    def print_product_receipt(self, shop):
        for product, quantity in self.product_cart.items():
            cost = shop.products[product] * quantity
            print(f"{product.capitalize()}: {quantity} x ${shop.products[product]:.2f} = ${cost:.2f}")

    def go_home(self):
        self.location = self.home_location
        print(f"{self.name} arrived back home with ${self.money:.2f} remaining.\n")
