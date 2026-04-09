import datetime
import json
import os

from app.shops import *
from app.сustomers import *


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")
def shop_trip() -> None:
    with open(CONFIG_PATH, "r") as config:
        trip = json.load(config)
    customers = create_customers(trip["customers"])
    shops = create_stores(trip["shops"])
    for name, customer in customers.items():
        calculated_product_list = customer.calculate_products(shops)
        calculated_road_list = customer.calculate_road(shops, trip["FUEL_PRICE"])
        total_price = total(calculated_product_list, calculated_road_list)
        best_shop = min(total_price, key=total_price.get)
        print(f"{name} has {customer.money} dollars")
        for shop_name, price in total_price.items():
            print(f"{name}'s trip to the {shop_name} costs {price}")
        if customer.money >= total_price[best_shop]:
            print(f"{customer.name} rides to {best_shop}\n")
            customer.ride_to_shop(shops[best_shop].location)
            print(f"Date: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}")
            print(f"Thanks, {name}, for your purchase!")
            print(f"You have bought:")
            for product in calculated_product_list[best_shop]:
                price = calculated_product_list[best_shop][product]
                print(f"{customer.product_cart[product]} {product}s for {price:g} dollars")
            print(f"Total cost is {sum(calculated_product_list[best_shop].values())} dollars")
            print("See you again!\n")
            customer.ride_home()
            print(f"{customer.name} rides home")
            customer.money -= total_price[best_shop]
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
