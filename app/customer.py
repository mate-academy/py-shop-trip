import datetime
import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, customer_info: dict) -> None:
        self.name = customer_info["name"]
        self.product_cart = customer_info["product_cart"]
        self.location = customer_info["location"]
        self.money = customer_info["money"]
        self.car = Car(customer_info["car"]["brand"],
                       customer_info["car"]["fuel_consumption"])

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = math.dist(self.location, shop.location)
        fuel_consumption = self.car.fuel_consumption
        fuel_to_shop = (distance / 100) * fuel_consumption * fuel_price
        products_cost = self.calculate_products_cost(shop.products)

        return 2 * fuel_to_shop + products_cost

    def calculate_products_cost(self, shop_products: dict) -> float:
        total = 0
        for product, quantity in self.product_cart.items():
            if product in shop_products:
                price_per_unit = shop_products[product]
                total += price_per_unit * quantity
        return total

    def print_about_purchase(self, products: dict, total_cost: float) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {current_time}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in self.product_cart.items():
            print(f"{quantity} {product}s "
                  f"for {quantity * products[product]} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")

    def make_purchase(self, shop: Shop) -> None:
        products_cost = self.calculate_products_cost(shop.products)
        trip_cost = self.calculate_trip_cost(shop, shop.fuel_price)
        total_cost = products_cost + trip_cost

        if self.money >= total_cost:
            self.money -= total_cost
            self.print_about_purchase(shop.products, total_cost)
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in {shop.name}.")

    def return_home(self) -> None:
        print(f"\n{self.name} rides home")
        print(f"{self.name} now has {self.money:.2f} dollars")
