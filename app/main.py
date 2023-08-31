import json
import os

from app.customer import Customer
from app.shop import Shop


current_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_dir, "config.json")


def shop_trip() -> None:
    with open(config_path, "r") as config:
        data = json.load(config)
    customers = Customer.get_customers_list(data)
    shops = Shop.get_shops_list(data)
    fuel_price = data["FUEL_PRICE"]
    for customer in customers:
        if customer.go_shopping(
            *(
                customer.find_the_cheapest_shop(
                    shops=shops, fuel_price=fuel_price
                )
            )
        ):
            customer.go_home()


if __name__ == "__main__":
    shop_trip()
