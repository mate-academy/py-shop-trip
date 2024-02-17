import json
import math
import os
from pathlib import Path

from app.car import Car
from app.customer import Customer
from app.shop import Shop

config_path = os.path.join(Path(__file__).resolve().parent, "config.json")
with open(config_path, "r") as file:
    info_from_file = json.load(file)

customers = {}

for customer in info_from_file["customers"]:
    customers[customer["name"]] = Customer(
        customer["name"],
        customer["product_cart"],
        customer["location"],
        customer["money"],
        Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
    )

shops = {}

for shop in info_from_file["shops"]:
    shops[shop["name"]] = Shop(
        shop["name"],
        shop["location"],
        shop["products"]
    )

cost_of_trip = {}


def calculate_cost_of_trip(
        customer: Customer,
        shop: Shop
) -> None:
    distance = math.sqrt(
        (customer.location[0] - shop.location[0]) ** 2
        + (customer.location[1] - shop.location[1]) ** 2
    )
    fuel_cost = round(
        2
        * distance
        * customer.car.fuel_consumption
        / 100
        * info_from_file["FUEL_PRICE"], 2
    )
    cart_cost = 0
    for product_name, product_cost in customer.product_cart.items():
        cart_cost += product_cost * shop.products[product_name]
    return fuel_cost + cart_cost


def find_best_trip(customer: Customer) -> Shop:
    result = {
        shop: calculate_cost_of_trip(customer, shop) for shop in shops.values()
    }
    min_cost = min(result.values())
    for shop, cost in result.items():
        if cost == min_cost:
            return shop


def print_receipt(customer: Customer, shop: Shop) -> None:
    current_time = "04/01/2021 12:33:41"
    print(f"\nDate: {current_time}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought:")
    total_cost = 0
    for product, quantity in customer.product_cart.items():
        product_cost = quantity * shop.products[product]
        total_cost += product_cost
        if int(product_cost) == product_cost:
            product_cost = int(product_cost)
        print(f"{quantity} {product}s for {product_cost} dollars")
    print(f"Total cost is {total_cost} dollars")
    print("See you again!")
