import json
import datetime
import sys
from pathlib import Path

from app.customer import Customer
from app.shop import Shop

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG = f"{BASE_DIR}/app/config.json"


def shop_trip() -> None:
    with open(CONFIG) as file:
        config = json.load(file)
    fuel_price = config["FUEL_PRICE"]
    closest_shop = None
    for customer_dict in config["customers"]:
        customer = Customer(**customer_dict)
        ride_cost = sys.maxsize

        print(f"{customer.name} has {customer.money} dollars")

        for shop_dict in config["shops"]:
            shop = Shop(**shop_dict)
            shop_ride_cost = customer.calculate_ride_price(shop.location,
                                                           fuel_price)
            shop_ride_cost += customer.calculate_products_price(shop)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {shop_ride_cost}")
            if ride_cost > shop_ride_cost:
                ride_cost = shop_ride_cost
                closest_shop = shop

        if customer.money < ride_cost:
            print(f"{customer.name} doesn\'t have enough "
                  f"money to make a purchase in any shop")
        else:
            customer.money -= ride_cost
            print(f"{customer.name} rides to {closest_shop.name}")
            print("\nDate:",
                  datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product, quantity in customer.product_cart.items():
                cost = quantity * closest_shop.products[product]
                if isinstance(cost, float):
                    if cost.is_integer():
                        cost = int(cost)
                print(f"{quantity} {product}s for {cost} dollars")
            print(f"Total cost is "
                  f"{customer.calculate_products_price(closest_shop)} dollars")
            print("See you again!\n")

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")
