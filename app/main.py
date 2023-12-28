from app.customer import Customer
from app.shop import Shop
from app.car import Car

import json
import os


def shop_trip() -> None:
    config_file = "config.json"
    file_path = os.path.abspath(__file__)
    config_file_path = os.path.join(os.path.dirname(file_path), config_file)
    with open(config_file_path, "r") as f:
        file_content = json.load(f)
        for i in file_content["customers"]:
            customer = Customer(i["name"], i["money"])
            car = Car(i["car"]["brand"], i["location"],
                      file_content["FUEL_PRICE"], i["car"]["fuel_consumption"])
            customer.money_sum()
            if customer.cost_trip(car, i["product_cart"],
                                  file_content["shops"]) is False:
                break
            else:
                Shop.listing_food(i["product_cart"],
                                  file_content["shops"],
                                  customer.picked_shop)
                customer.rides_home()
