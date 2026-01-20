import sys
import datetime
from math import sqrt
import json
from app.shop import Shop


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip_price(
            self, shop: Shop,
            fuel_price: float
    ) -> int | float:

        dx = shop.location[0] - self.location[0]
        dy = shop.location[1] - self.location[1]
        distance_km = sqrt(dx ** 2 + dy ** 2)

        fuel_cost = self.car.fuel_consumption * distance_km / 100 * fuel_price

        product_cost = sum(
            shop.products[product] * self.product_cart[product]
            for product in self.product_cart
            if product in shop.products
        )

        cost = fuel_cost + product_cost + fuel_cost

        return cost

    def buy_products(self, shop: Shop) -> None:

        current_date = datetime.datetime.now()
        current_date = current_date.strftime("%d/%m/%Y %H:%M:%S")
        product_cost = {
            product: [self.product_cart[product], shop.products[product]]
            for product in self.product_cart
            if product in shop.products
        }
        total = sum(
            shop.products[product] * self.product_cart[product]
            for product in self.product_cart
            if product in shop.products
        )

        print(f"Date: {current_date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for product in product_cost:
            purchase = round(product_cost[product][0]
                             * product_cost[product][1], 1)
            if purchase == 3.0:
                purchase = f"{round(purchase, 1)}".rstrip("0").rstrip(".")
            print(f"{product_cost[product][0]}"
                  f" {product}s "
                  f"for {purchase}"
                  f" dollars")
        print(f"Total cost is {total} dollars")
        print("See you again!", end="\n\n")

    def change_wallet(self, cost_of_trip: int | float) -> None:
        self.money -= cost_of_trip


def get_data_from_json(filename: str) -> dict:
    with open(filename, "r") as json_file:
        data = json.load(json_file)

    return data


def process_data(data_dict: dict) -> tuple:

    fuel_price = data_dict.get("FUEL_PRICE", None)
    if fuel_price is None:
        sys.exit("FUEL_PRICE not found in config.json")

    customers_list = data_dict.get("customers", [])
    if not customers_list:
        sys.exit("Customers not found in config.json")

    shops_list = data_dict.get("shops", [])
    if not shops_list:
        sys.exit("Shops not found in config.json")

    for index, customer in enumerate(customers_list):
        customer = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(customer["car"]["brand"], customer["car"]["fuel_consumption"]),
        )
        customers_list[index] = customer

    for index, shop in enumerate(shops_list):
        shop = Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        shops_list[index] = shop

    return fuel_price, customers_list, shops_list
