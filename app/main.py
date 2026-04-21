import json
import datetime
import os

from app.customer import Customer
from app.shop import Shop

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(BASE_DIR, "config.json")


def shop_trip() -> None:
    with open(config_path) as config:
        data = json.load(config)

    fuel_price = data["FUEL_PRICE"]

    customers = Customer.make_customers(data["customers"])
    shops = Shop.make_shops(data["shops"])

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        shops_prices = [
            customer.calculate_all_trip(shop, fuel_price)
            for shop in shops
        ]
        cheapest_shop = min(shops_prices, key=lambda s: s[0])
        if customer.money < cheapest_shop[0]:
            print(f"{customer.name} doesn't have enough money to make a "
                  "purchase in any shop")
            continue
        customer.ride_to_cheapest_shop(cheapest_shop[1])
        customer.money -= cheapest_shop[0]
        print()
        frmt = "%d/%m/%Y %H:%M:%S"
        print(f"Date: {datetime.datetime.now().strftime(frmt)}")
        cheapest_shop[1].print_check(
            customer.name,
            customer.products_want
        )
        print()
        customer.ride_to_home()
        print()


if __name__ == "__main__":
    shop_trip()
