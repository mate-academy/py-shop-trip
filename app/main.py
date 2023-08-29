import json
import os

from app.customer import load_customers
from app.shop import load_shops

absolute_path = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(absolute_path, "config.json")


def shop_trip():
    with open(FILE, "r") as f:
        data = json.load(f)

    customers = load_customers(data)
    shops = load_shops(data)
    cost_of_fuel = data["FUEL_PRICE"]

    for customer in customers:
        customer_home = customer.location
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop, total_price = customer.find_the_cheapest_shop(shops, cost_of_fuel)
        if total_price > customer.money:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
            continue

        customer.ride_to_shop(cheapest_shop)

        cheapest_shop.purchase(customer)

        customer.ride_to_home(customer_home)

        customer.count_money_after_shop(total_price)


shop_trip()
