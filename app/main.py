import json
from typing import List, Dict
import datetime
import os
from decimal import Decimal

from app.customer import Customer
from app.shop import Shop
from app.car import trip_cost


def shop_trip() -> None:
    with open(
            os.path.join(os.path.dirname(__file__), "config.json"),
            "r"
    ) as config_file:
        config_data = json.load(config_file)

    fuel_price = config_data["FUEL_PRICE"]
    customers: List[Customer] = []
    shops: Dict[Shop] = {}

    for customer in config_data["customers"]:
        customers.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        ))

    for shop in config_data["shops"]:
        shops[shop["name"]] = (Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ))

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        lowest_price_dict = {}
        lowest_shop = ""

        for shop in shops.values():
            trip_cost_for_one_direction = trip_cost(
                customer.location,
                shop.location,
                fuel_price,
                customer.car["fuel_consumption"]
            )
            shop_total_price = 0
            for product, product_amount in customer.product_cart.items():
                shop_total_price += (Decimal(product_amount)
                                     * Decimal(shop.products[product]))
            total_price_trip = (
                Decimal(shop_total_price)
                + Decimal(trip_cost_for_one_direction) * 2
            ).quantize(Decimal("0.01"))
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_price_trip}")

            if customer.money >= total_price_trip:
                lowest_price_dict[shop.name] = total_price_trip

        if lowest_price_dict:
            lowest_shop = min(lowest_price_dict, key=lowest_price_dict.get)
            print(f"{customer.name} rides to {lowest_shop}\n")
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")

        if lowest_shop:
            customer.location = shops[lowest_shop].location
            datetime_format = "%d/%m/%Y %H:%M:%S"
            print(f"Date: {datetime.datetime.now().strftime(datetime_format)}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            total_price_shop = 0
            for product, product_amount in customer.product_cart.items():
                product_price = ((product_amount
                                 * Decimal(shops[lowest_shop]
                                           .products[product]))
                                 .quantize(Decimal("0.01")))
                product_price = Decimal(product_price).normalize()
                print(f"{product_amount} "
                      f"{product}s for "
                      f"{product_price}"
                      f" dollars")
                total_price_shop += product_price
            print(f"Total cost is {total_price_shop} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            result_money = ((Decimal(customer.money)
                            - min(lowest_price_dict.values()))
                            .quantize(Decimal("0.01")))
            customer.money = result_money
            print(f"{customer.name} now has "
                  f"{result_money} dollars\n")
