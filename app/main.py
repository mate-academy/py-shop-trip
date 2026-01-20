import json
import os

from app.customer.customer import Customer
from app.shop.shop import Shop


current_directory = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(current_directory, "config.json")


def shop_trip() -> None:
    with open(FILE_PATH, "r") as source:
        config = json.load(source)

    fuel_cost = config["FUEL_PRICE"]
    customers = [Customer.from_dict(cust) for cust in config["customers"]]
    shops = [Shop.from_dict(shop) for shop in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        cheapest_cost = 0
        for shop in shops:
            cost = customer.calculate_fuel_cost(shop.location, fuel_cost)
            cost += shop.calculate_price_for_cart(customer.product_cart)

            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {round(cost, 2)}"
            )

            if not cheapest_cost or cost < cheapest_cost:
                cheapest_cost = cost
                cheapest_shop = shop

        if customer.money < cheapest_cost:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue

        customer.money -= cheapest_cost
        print(f"{customer.name} rides to {cheapest_shop.name}\n")
        cheapest_shop.purchase(customer)

        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {customer.money} dollars\n")
