from app.customer import Customer
from math import sqrt
import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.check_price = None
        self.name = name
        self.location = location
        self.products = products
        self.full_price = float("inf")

    def to_shop(self, customer: Customer) -> None:
        print(f"{customer.name} rides to {self.name}\n")

    def check(self, customer: Customer) -> None:
        print("Date:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought: "
        )
        for product, price in self.products.items():
            if product in customer.product_cart:
                print(
                    f"{customer.product_cart[product]} {product}s "
                    f"for {customer.product_cart[product] * price} dollars"
                )
        print(
            f"Total cost is {self.check_price} dollars\nSee you again!\n"
        )

    def trip_price_counting(
        self, customer: Customer, fuel_price: float
    ) -> None:
        distance = sqrt(
            (customer.location[0] - self.location[0]) ** 2
            + (customer.location[1] - self.location[1]) ** 2
        )
        fuel = (distance * customer.car.fuel_consumption) / 100 * fuel_price
        full_price = fuel * 2
        for product, price in self.products.items():
            if product in customer.product_cart:
                full_price += customer.product_cart[product] * price
        print(
            f"{customer.name}'s trip to the {self.name} "
            f"costs {round(full_price, 2)}"
        )
        self.full_price = round(full_price, 2)
        self.check_price = round(self.full_price - fuel * 2, 2)
