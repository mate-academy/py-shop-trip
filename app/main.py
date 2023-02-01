from __future__ import annotations
import json
from app.shop import Shop
from app.customer import Customer
import datetime


def shop_trip() -> None:
    with open("app/config.json", "r") as data:
        json_input = json.load(data)
    fuel_price = json_input["FUEL_PRICE"]
    customers = Customer.create_customers(json_input["customers"])
    shops = Shop.create_shop(json_input["shops"])
    for customer in customers:
        customer.print_money_remainder()
        shop_to_visit = customer.choose_ideal_shop(shops, fuel_price)
        if shop_to_visit is None:
            continue
        customer.charge_for_trip(shop_to_visit, fuel_price)
        print(
            f"Date: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        )
        print(f"Thanks, {customer.name}, for you purchase!")
        shop_to_visit.sell_products(customer.product_cart)
        print("See you again!\n")

        products_price = shop_to_visit.sell_products(
            customer.product_cart, False
        )
        customer.money -= products_price
        customer.ride_home_and_show_remainder()


if __name__ == "__main__":

    shop_trip()
