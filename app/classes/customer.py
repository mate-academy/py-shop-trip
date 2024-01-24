import datetime
from app.classes.car import Car
from app.classes.shop import Shop
from math import sqrt


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car

    ) -> None:
        self.name = name
        self.location = location
        self.product_cart = product_cart
        self.money = money
        self.car = car

    def calculate_trip_cost(self, shop: Shop) -> int | float:
        distance = sqrt(pow(self.location[0] - shop.location[0], 2)
                        + pow(self.location[1] - shop.location[1], 2))
        fuel_cost = ((self.car.fuel_consumption / 100)
                     * self.car.fuel_price * distance * 2)
        cost_of_products = sum(
            amount * shop.products[product]
            for product, amount in self.product_cart.items()
            if product in shop.products
        )
        return round(fuel_cost + cost_of_products, 2)

    def print_receipt(self, shop: Shop) -> str:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        receipt = (f"Date: {date}\n"
                   f"Thanks, {self.name}, for your purchase!\n"
                   f"You have bought:\n")
        total_sum = 0
        for product, amount in self.product_cart.items():
            if product in shop.products:
                cost = amount * shop.products[product]
                if cost == int(cost):
                    cost = int(cost)
                total_sum += cost
                receipt += f"{amount} {product + 's'} for {cost} dollars\n"
        receipt += (f"Total cost is {total_sum} dollars\n"
                    "See you again!")
        return receipt
