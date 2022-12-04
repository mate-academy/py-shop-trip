import math
import datetime
from app.customers import Customers


class Calculater:
    def __init__(
            self,
            customer: Customers,
            shops: list,
            fuel_price: float
    ) -> None:
        self.customer = customer
        self.shops = shops
        self.fuel_price = fuel_price

    def calculate(self) -> None:
        customer_location = self.customer.location
        fuel_consumption = self.customer.car["fuel_consumption"]
        total_value = 1_000_000
        best_shop = None
        product_price = 0

        for shop in self.shops:
            shop_location = shop.location

            distance = math.dist(customer_location, shop_location)
            price_ride = round(
                distance * self.fuel_price * 2 * (fuel_consumption / 100), 2
            )
            check_product = 0
            for product in self.customer.product_cart:
                check_product += \
                    self.customer.product_cart[product] * shop.products[product]

            total_cost = round((check_product + price_ride), 2)
            print(f"{self.customer.name}'s trip to the {shop.name} costs {total_cost}")

            if total_cost < total_value:
                total_value = total_cost
                best_shop = shop
                product_price = check_product

        if total_value < self.customer.money:
            print(f"{self.customer.name} rides to {best_shop.name}\n")

            date_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"Date: {date_time}")
            print(f"Thanks, {self.customer.name}, for you purchase!")
            print("You have bought: ")

            for product, amount in self.customer.product_cart.items():
                print(f"{amount} {product}s for "
                      f"{amount * best_shop.products[product]} dollars")

            print(f"Total cost is {product_price} dollars")
            print("See you again!\n")

            print(f"{self.customer.name} rides home")
            self.customer.money -= total_value
            print(f"{self.customer.name} now has {self.customer.money} dollars\n")

        else:
            print(f"{self.customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
