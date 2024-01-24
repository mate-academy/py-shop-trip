import datetime

from app.data.json_extraction import FUEL_PRICE
from app.objects.shop import Shop
from app.objects.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list[int],
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def trip_cost(self, shop: Shop) -> float:
        distance = ((self.location[0] - shop.location[0]) ** 2
                    + (self.location[1] - shop.location[1]) ** 2) ** .5
        fuel_cost = ((self.car.fuel_consumption / 100)
                     * FUEL_PRICE * distance * 2)
        cart_total = sum(self.product_cart[product] * shop.products[product]
                         for product in self.product_cart.keys())
        return round(fuel_cost + cart_total, 2)

    def print_receipt(self, shop: Shop) -> None:
        print("\nDate:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        for product, amount in self.product_cart.items():
            product_total = shop.products[product] * amount
            if product_total == int(product_total):
                product_total = int(product_total)
            print(f"{amount} {product}s for "
                  f"{product_total} dollars")

        cart_total = sum(self.product_cart[product] * shop.products[product]
                         for product in self.product_cart.keys())

        print(f"Total cost is {cart_total} dollars")
        print("See you again!\n")
