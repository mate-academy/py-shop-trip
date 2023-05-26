from app.customer import Customer
from app.shop import Shop
from os import path
import json
from datetime import datetime


def shop_trip() -> None:
    parent_dir = path.dirname(__file__)
    with open(path.join(parent_dir, "config.json"), "r") as f:
        data = json.load(f)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(**customer) for customer in data["customers"]]
    shops = [Shop(**shop) for shop in data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        shops_costs = {}
        for shop in shops:
            fuel_cost = customer.cost_to_shop(shop, fuel_price)
            products_cost = customer.cost_of_products(shop)
            full_cost = round(fuel_cost + products_cost, 2)

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {full_cost}")
            shops_costs[shop.name] = {
                "shop_instance": shop,
                "shop_cost": full_cost
            }
        best_shop = shops_costs[
            min(shops_costs, key=lambda x: shops_costs[x]["shop_cost"])
        ]
        if customer.money >= best_shop["shop_cost"]:
            shop = best_shop["shop_instance"]
            amount_and_cost = customer.shopping(shop)
            specified_date = datetime.strptime(
                "04/01/2021 12:33:41", "%d/%m/%Y %H:%M:%S"
            )
            print(f"{customer.name} rides to {shop.name}\n")

            home_location = customer.location
            customer.location = shop.location

            print(f"Date: {specified_date.strftime('%d/%m/%Y %H:%M:%S')}\n"
                  f"Thanks, {customer.name}, for your purchase!\n"
                  f"You have bought: ")
            for index, product_name in enumerate(customer.product_cart.keys()):
                print(f"{amount_and_cost[product_name][0]} "
                      f"{product_name}s for {amount_and_cost[product_name][1]}"
                      f" dollars")
            print(f"Total cost is {amount_and_cost['total_cost']} dollars\n"
                  f"See you again!\n\n"
                  f"{customer.name} rides home")

            customer.location = home_location

            print(f"{customer.name} now has "
                  f"{customer.money - best_shop['shop_cost']} dollars\n")
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
