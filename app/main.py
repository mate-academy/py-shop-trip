import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as json_config:
        config = json.load(json_config)

    fuel_price = config["FUEL_PRICE"]
    shops = Shop.create_shops(config["shops"])
    customers = Customer.create_customers(config["customers"])

    for customer in customers:
        shop = customer.find_the_cheapest_option(shops, fuel_price)
        if customer.has_enough_money:
            customer.visit_shop(shop)
            customer.go_home()
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )


if __name__ == '__main__':
    shop_trip()
