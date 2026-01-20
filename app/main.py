from app.customer import Customer
from app.car import Car
from app.shop import Shop
from app.calculations import calculate_trip_cost

import json
import datetime
import os


def shop_trip() -> None:

    config_file_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_file_path, "r") as config:
        config_data = json.load(config)

    customers_data = config_data["customers"]
    shops_data = config_data["shops"]
    fuel_price = config_data["FUEL_PRICE"]

    customers = [Customer(name=customer_data["name"],
                          product_cart=customer_data["product_cart"],
                          location=customer_data["location"],
                          money=customer_data["money"],
                          car=Car(**customer_data["car"]))
                 for customer_data in customers_data]
    shops = [Shop(**shop_data) for shop_data in shops_data]

    for customer in customers:
        cheapest_shop = None
        cheapest_cost = float("inf")

        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            cost = calculate_trip_cost(customer, shop, fuel_price)
            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {cost:.2f}".rstrip("0").rstrip(".")
            )
            if cost < cheapest_cost and customer.money >= cost:
                cheapest_cost = cost
                cheapest_shop = shop

        if cheapest_shop is not None:
            customer.location = cheapest_shop.location
            customer.money -= cheapest_cost
            print(f"{customer.name} rides to {cheapest_shop.name}\n")

            purchase_time = datetime.datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            )

            print(f"Date: {purchase_time}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")

            total_product_cost = 0
            for product, quantity in customer.product_cart.items():
                product_cost = cheapest_shop.products[product] * quantity
                total_product_cost += product_cost
                print(
                    f"{quantity} {product}s for "
                    f"{product_cost}".rstrip("0").rstrip(".") + " dollars"
                )

            print(f"Total cost is {total_product_cost} dollars")
            print("See you again!")

            print(f"\n{customer.name} rides home")
            print(
                f"{customer.name} now has "
                f"{customer.money:.2f}".rstrip("0").rstrip(".") + " dollars\n"
            )
        else:
            print(
                f"{customer.name} doesn't have enough "
                "money to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
