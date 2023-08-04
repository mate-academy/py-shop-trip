import datetime
import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str, money: int, car: Car, product_cart: dict, customer_location: list) -> None:
        self.name = name
        self.money = money
        self.car = car
        self.product_cart = product_cart
        self.customer_location = customer_location

    def calculate_road(self, shop: Shop, fuel_price: float) -> float:
        distance = math.dist(self.customer_location, shop.shop_location)

        return distance * (self.car.fuel_consumption / 100) * fuel_price * 2

    def products_cost(self, product_cart):
        total = 0
        for product in product_cart:
            total += self.product_cart[product]
        return total

    def print_the_purchase_receipt(self, cheapest_shop):
        print(f"\nDate: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")
        for product, amount in cheapest_shop.products.items():
            count = self.product_cart.get(product, 0)
            if count > 0:
                print(f"{count} {product}s for {count * amount} dollars")
        print(f"Total cost is {self.products_cost(self.product_cart)} dollars")
        print("See you again!\n")
