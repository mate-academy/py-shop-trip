import math
import datetime
from decimal import Decimal


class Customer:
    def __init__(
            self,
            name: str,
            money: int,
            location: list,
            product_cart: dict,
            car: str,
            car_fuel_consumption: float
    ):
        self.name = name
        self.money = money
        self.location = location
        self.product_cart = product_cart
        self.car = car
        self.car_fuel_consumption = car_fuel_consumption

    def calculate_trip_price(
            self,
            fuel_price: float,
            shop_location: list
    ):
        distance = round(math.dist(self.location, shop_location), 2)
        fuel_per_km = self.car_fuel_consumption / 100
        price_for_distance = distance * fuel_per_km * fuel_price
        if int((price_for_distance * 2) * 1000) % 10 > 5:
            return price_for_distance * 2
        return int((price_for_distance * 2) * 100) / 100

    def calculate_price_for_products(
            self,
            products: dict
    ):
        price_dict = {
            key: self.product_cart[key] * products[key]
            for key, value in self.product_cart.items()
        }
        all_price = sum([value for value in price_dict.values()])
        return price_dict, all_price

    def print_shoping_message(
            self,
            total_cost: float,
            price_for_fuel: float,
            bill: dict,
            shop_name: str
    ):
        print(
            f"{self.name} rides to {shop_name}\n\n"
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {self.name}, for you purchase!\n"
            f"You have bought: "
        )

        for key, value in bill.items():
            print(f"{self.product_cart[key]} {key}s for {value} dollars")

        print(
            f"Total cost is {total_cost - price_for_fuel} dollars\n"
            "See you again!\n\n"
            f"{self.name} rides home\n"
            f"{self.name} now has {(self.money - total_cost):.2f} dollars\n"
        )
