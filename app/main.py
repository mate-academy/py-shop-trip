import json
import os.path

from decimal import Decimal

from app.customer import Customer, return_customers
from app.shop import Shop, return_shops


def shop_trip() -> None:
    config_file_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_file_path, "r") as source_file:
        source_data = json.load(source_file)
    fuel_price: Decimal = Decimal(str(source_data["FUEL_PRICE"]))
    customers_source: list = source_data["customers"]
    shops_source: list = source_data["shops"]

    customers_list: list[Customer] = return_customers(customers_source)

    shops_list: list[Shop] = return_shops(shops_source)

    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        elect_shop, spent_money = customer.select_shop(shops_list, fuel_price)
        if elect_shop:
            home_location: list = customer.location
            customer.visit_shop(elect_shop)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{customer.money - spent_money} dollars\n")
            customer.location = home_location


if __name__ == "__main__":
    shop_trip()
