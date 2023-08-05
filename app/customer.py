import datetime

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str, money: int, car: Car, product_cart: dict, customer_location: list) -> None:
        self.name = name
        self.money = money
        self.car = car
        self.product_cart = product_cart
        self.location = customer_location

    def get_trip_price(self, fuel_price: int | float, shop: Shop) -> int | float:
        distance = (
                (
                        (shop.location[0] - self.location[0]) ** 2
                        + (shop.location[1] - self.location[1]) ** 2
                ) ** 0.5
        )
        fuel_cost = fuel_price * (
                self.car.fuel_consumption / 100
        ) * distance * 2
        products_price = self.get_product_price(shop)
        return round(fuel_cost + products_price, 2)

    def get_product_price(self, shop: Shop):
        return sum(
            [
                shop.products[product] * amount
                for product, amount in self.product_cart.items()
            ]
        )

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
