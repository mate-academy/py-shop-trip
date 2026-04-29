import math
import datetime

from app.car import Car
from app.shop import Shop
from app.product import Product


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int | float],
            money: int | float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = [
            Product(key, value) for key, value in product_cart.items()
        ]
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def distance_to_shop(self, other: Shop) -> int | float:
        return math.dist(self.location, other.location)

    def price_for_products(self, other: Shop) -> int | float:
        return sum(
            product * price for product, price in zip(
                self.product_cart, other.products
            )
        )

    def price_for_shop_trip(
            self,
            other: Shop,
            fuel_price: int | float
    ) -> int | float:
        return round(
            self.price_for_products(other)
            + (self.car.fuel_price_distance(
                fuel_price, self.distance_to_shop(other)) * 2
               ),
            2)

    def receipt(self, shop: Shop) -> None:
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        )
        print(f"Thanks, {self.name}, for your purchase!\nYou have bought:")
        for product, product_price in zip(self.product_cart, shop.products):
            print(
                f"{product.number} "
                f"{product.name}s for {product * product_price} dollars"
            )
        print(
            f"Total cost is {self.price_for_products(shop)} dollars\n"
            f"See you again!\n"
        )
