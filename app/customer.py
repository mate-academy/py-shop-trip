from math import sqrt

from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: int | float,
        car: dict,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def find_best_shop(
        self, shops: list[Shop], fuel_price: int | float
    ) -> tuple:
        print(f"{self.name} has {self.money} dollars")

        best_shop = None
        best_price = None

        for shop in shops:
            trip_price = 0
            distance = sqrt(
                (self.location[0] - shop.location[0]) ** 2
                + (self.location[1] - shop.location[1]) ** 2
            )
            trip_price += (
                distance * self.car.fuel_consumption / 100 * fuel_price
            ) * 2

            for product, quantity in self.product_cart.items():
                trip_price += quantity * shop.products[product]

            trip_price = round(trip_price, 2)

            print(
                f"{self.name}'s trip to the {shop.name} costs " f"{trip_price}"
            )

            if trip_price <= self.money:
                if best_price and trip_price < best_price:
                    best_price = trip_price
                    best_shop = shop
                if not best_price:
                    best_price = trip_price
                    best_shop = shop

        if best_shop:
            return best_shop, best_price

        print(
            "Monica doesn't have enough money to " "make a purchase in any shop"
        )
        return None, None
