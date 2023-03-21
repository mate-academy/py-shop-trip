import json
from app.car import Car
from app.shop import Shop, shop_list
import datetime


class Customer:
    def __init__(self, customer_info: dict) -> None:
        self.name = customer_info["name"]
        self.product_cart = customer_info["product_cart"]
        self.location = customer_info["location"]
        self.money = customer_info["money"]
        self.car = Car(customer_info["car"])

    def calculate_fuel_cost(self, shop_location: list[int]) -> float:
        distance = (
            ((self.location[0] - shop_location[0]) ** 2
             + (self.location[1] - shop_location[1]) ** 2) ** 0.5
        )
        fuel_cost = self.car.fuel_consumption * distance / 100 * FUEL_PRICE

        return fuel_cost * 2

    def calculate_products_cost(self, products_in_shop: dict) -> float:
        product_cost = 0
        for product, amount in self.product_cart.items():
            product_cost += products_in_shop[product] * amount
        return product_cost

    def select_shop(self) -> tuple[Shop, int]:
        list_of_expenses = []

        for shop in shop_list:
            total_expenses = round(
                self.calculate_fuel_cost(shop.location)
                + self.calculate_products_cost(shop.products), 2
            )
            list_of_expenses.append(total_expenses)

            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {total_expenses}")

        cheapest_shop_index = list_of_expenses.index(min(list_of_expenses))
        selected_shop = shop_list[cheapest_shop_index]

        return selected_shop, list_of_expenses[cheapest_shop_index]

    def go_to_shop(self, shop: Shop) -> None:
        self.location = shop.location

        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %X')}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")

        for product, amount in self.product_cart.items():
            print(f"{amount} {product}s for "
                  f"{shop.products[product] * amount} dollars")

        total_cost = self.calculate_products_cost(shop.products)

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money - total_cost} dollars")


customer_list = []
with open("../config.json", "r") as file_in:
    data = json.load(file_in)

customers_info = data["customers"]
FUEL_PRICE = data["FUEL_PRICE"]

for customer in customers_info:
    customer_list.append(Customer(customer))
