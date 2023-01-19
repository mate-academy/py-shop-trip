from __future__ import annotations
import json
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as data:
        output = json.load(data)
    fuel_price = output["FUEL_PRICE"]
    customers = Customer.create_customers(output["customers"])
    shops = Shop.create_shops(output["shops"])
    for customer in customers:
        customer.print_money_remainder()
        shop_to_visit = customer.choose_shop(shops, fuel_price)
        if shop_to_visit is None:
            continue
        customer.charge_for_trip(shop_to_visit, fuel_price)
        shop_to_visit.sell_products(customer)
        customer.ride_home_and_show_remainder()


if __name__ == "__main__":

    shop_trip()
