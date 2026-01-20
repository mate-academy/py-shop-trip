import json
import os
from decimal import Decimal

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open(f"app{os.sep}config.json", "r") as file:
        trip_data = json.load(file)

    shops = []
    fuel_price = Decimal(str(trip_data["FUEL_PRICE"]))

    for shop_data in trip_data["shops"]:
        shops.append(Shop(**shop_data))

    for customer_data in trip_data["customers"]:
        customer_data["car_data"] = customer_data.get("car")
        del customer_data["car"]

        customer = Customer(**customer_data)

        print(f"{customer.name} has {customer.money} dollars")
        cheap_shop, cheap_cost = customer.find_cheapest(shops, fuel_price)

        if customer.money < cheap_cost:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            continue

        customer.ride_to(cheap_shop.location, cheap_shop.name)
        cheap_shop.prints_receipt(customer.product_cart, customer.name)
        customer.pay_and_back(cheap_cost)
