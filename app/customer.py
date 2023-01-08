from app.shop import Shop
from app.car import Car
import datetime


class Customer:
    def __init__(self, customer: dict) -> None:
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = customer["car"]

    def fuel_coast_for_trip(self, coast_per_liter: Car, shop: Shop) -> float:
        coast = self.car["fuel_consumption"] \
            * self.distance_to_shop(shop) \
            * coast_per_liter.fuel_price / 100
        return coast

    def distance_to_shop(self, shop: Shop) -> float:
        distance = (
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        ) ** 0.5
        return distance

    def coast_of_trip_to_shop(self, shop: Shop, coast_per_liter: Car) -> float:
        total_coast = self.fuel_coast_for_trip(coast_per_liter, shop) * 2
        total_coast += self.product_cart["milk"] * shop.products["milk"]
        total_coast += self.product_cart["bread"] * shop.products["bread"]
        total_coast += self.product_cart["butter"] * shop.products["butter"]
        return round(total_coast, 2)

    def go_shopping(self, shop: Shop, coast_per_liter: Car) -> None:
        customer_home = self.location.copy()
        print(f"{self.name} rides to {shop.name}")
        spend_money = self.coast_of_trip_to_shop(shop, coast_per_liter)
        print()
        self.location = shop.location
        data_of_purchase =\
            datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {data_of_purchase}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")
        total_coast_of_products = 0
        for product in self.product_cart:
            coast_of_product = self.product_cart[product] * \
                shop.products[product]
            print(
                f"{self.product_cart[product]} {product}s for"
                f" {coast_of_product} dollars"
            )
            total_coast_of_products += self.product_cart[product] * \
                shop.products[product]
        print(f"Total cost is {total_coast_of_products} dollars")
        self.money -= spend_money
        print("See you again!")
        print()
        print(f"{self.name} rides home")
        self.location = customer_home
        print(f"{self.name} now has {self.money} dollars")
        print()
