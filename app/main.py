import json
import os.path
from pathlib import Path

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    file_path = os.path.join(Path(__file__).parent, "config.json")
    with open(file_path) as config:
        config = json.load(config)

    fuel_price = config.get("FUEL_PRICE")
    customers = Customer.create_customers(config.get("customers"))
    shops = Shop.create_shops(config.get("shops"))

    for customer in customers:
        best_shop, enough_money = customer.choose_the_best_shop(
            shops_list=shops,
            fuel_price=fuel_price
        )
        home_location = customer.location
        customer.ride_to_the_shop(
            shop=best_shop,
            enough_money=enough_money,
            fuel_price=fuel_price
        )
        if enough_money:
            customer.buy_products(
                shop=best_shop,
            )
            customer.ride_to_home(
                home_location=home_location,
                fuel_price=fuel_price
            )


if __name__ == "__main__":
    shop_trip()
