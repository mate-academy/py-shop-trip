import json
import os

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    config_path = os.path.join("app", "config.json")
    with open(config_path, "r") as config:
        data = json.load(config)

    customers = [
        Customer.from_dict(customer) for customer in data["customers"]
    ]

    shops = [Shop.from_dict(shop) for shop in data["shops"]]
    fuel_price = data["FUEL_PRICE"]

    for customer in customers:
        shop, cost_of_the_trip = customer.choice_shop(shops, fuel_price)

        if customer.money < cost_of_the_trip:
            print(f"{customer.name} doesn't have"
                  f" enough money to make a purchase in any shop")
            continue

        print(f"{customer.name} rides to {shop.name}\n")
        customer.location = shop.location

        shop.purchase_receipt(customer)
        customer.come_back_home(cost_of_the_trip)


if __name__ == "__main__":
    shop_trip()
