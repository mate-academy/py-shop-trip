import json
import math
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file_json:
        file_data = json.load(file_json)

    shops_list = [Shop(shop["name"],
                       shop["location"],
                       shop["products"])
                  for shop in file_data["shops"]]

    customers_list = [Customer(customer["name"],
                               customer["product_cart"],
                               customer["location"],
                               customer["money"],
                               customer["car"])
                      for customer in file_data["customers"]]

    fuel_price = file_data["FUEL_PRICE"]

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        cost_trip = {}
        for shop in shops_list:
            distance = math.dist(customer.location, shop.location)

            cost_trip[shop] = round(
                customer.cost_trip(
                    distance, fuel_price) + customer.sum_products(
                    shop.products), 2)
            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{cost_trip[shop]}")

        if customer.money > min(cost_trip.values()):
            cheaper_shop = min(cost_trip, key=cost_trip.get)
            print(f"{customer.name} rides to {cheaper_shop.name}\n")

            total_spend = cheaper_shop.receipt(customer)
            print(f"Total cost is {total_spend} dollars\nSee you again!")
            print()
            print(f"{customer.name} rides home"
                  f"\n{customer.name} now has "
                  f"{customer.money - cost_trip[cheaper_shop]} dollars")
            print()

        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")


shop_trip()
