import json

from pathlib import Path

from app.customer import Customer
from app.shop import Shop

BASE_DIR = Path(__file__).resolve().parent


def shop_trip():
    with open(BASE_DIR / "config.json") as json_file:
        data = json.load(json_file)

    shop_dict = {}

    for person in data["customers"]:
        customer = Customer(
            person["name"],
            person["money"],
            person["product_cart"],
            person["location"],
            person["car"]["fuel_consumption"]
        )
        print(f"{customer.name} has {customer.money} dollars")

        for shop in data["shops"]:
            shop = Shop(
                shop["name"],
                shop["products"],
                shop["location"]
            )

            money_needed_to_buy_products = customer.count_expenses(
                shop,
                data["FUEL_PRICE"]
            )
            shop_dict[shop] = money_needed_to_buy_products
            print(f"{customer.name}'s trip to the {shop.name} costs "
                  f"{money_needed_to_buy_products}")

        cheapest_shop = min(shop_dict, key=shop_dict.get)

        if customer.money < shop_dict[cheapest_shop]:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
        else:
            customer.going_to_shop(cheapest_shop, shop_dict[cheapest_shop])
