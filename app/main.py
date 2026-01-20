import json
import os.path

from decimal import Decimal

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    config_file_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_file_path, "r") as file:
        config = json.load(file)
        shops = config["shops"]
        customers = config["customers"]
        shops_list = Shop.shops_list(shops)
        fuel_price: Decimal = Decimal(str(config["FUEL_PRICE"]))
        customers_list = Customer.list_of_customers(customers)
        for customer in customers_list:
            print(f"{customer.name} has {customer.money} dollars")
            cheap_shop, cheap_price = customer.cheapest_trip(shops_list,
                                                             fuel_price)
            if cheap_shop:
                home = customer.location
                customer.visit_shop(cheap_shop)
                print(f"{customer.name} rides home")
                print(f"{customer.name} now has "
                      f"{customer.money - cheap_price} dollars\n")
                customer.location = home


if __name__ == "__main__":
    shop_trip()
