import json
import os
import datetime
from app.customer import define_customers
from app.shop import define_shops


current_dir = os.path.dirname(os.path.abspath(__file__))
config_file_path = os.path.join(current_dir, "config.json")


def shop_trip() -> None:
    with open(config_file_path, "r") as file:
        data = json.load(file)
    fuel_price = data["FUEL_PRICE"]
    customers = define_customers()
    shops = define_shops()
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            price = customer.price_for_trip(shop, fuel_price)
            print(f"{customer.name}'s trip to the {shop.name} costs {price}")
        cheapest = customer.define_cheapest(shops, fuel_price)
        if customer.money < customer.price_for_trip(cheapest, fuel_price):
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            continue
        print(f"{customer.name} rides to {cheapest.name}")
        print()
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        milk_price = customer.product_cart["milk"] * cheapest.products["milk"]
        if isinstance(milk_price, float) and milk_price.is_integer():
            milk_price = int(milk_price)
        bread_price = (customer.product_cart["bread"]
                       * cheapest.products["bread"])
        if isinstance(bread_price, float) and bread_price.is_integer():
            bread_price = int(bread_price)
        butter_price = (customer.product_cart["butter"]
                        * cheapest.products["butter"])
        if isinstance(butter_price, float) and butter_price.is_integer():
            butter_price = int(butter_price)
        total = milk_price + bread_price + butter_price
        rest = customer.money - customer.price_for_trip(cheapest, fuel_price)
        print(f"You have bought:\n"
              f"{customer.product_cart["milk"]} milks for "
              f"{milk_price} dollars\n"
              f"{customer.product_cart["bread"]} breads for "
              f"{bread_price} dollars\n"
              f"{customer.product_cart["butter"]} butters for "
              f"{butter_price} dollars\n"
              f"Total cost is {total} dollars\n"
              f"See you again!")
        print()
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has {rest} dollars")
        print()
