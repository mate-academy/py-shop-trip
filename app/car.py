import json
import os
import math
from app.shop import Shop


current_directory = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_directory, "config.json")
customers = []
with open(relative_path, "r") as file:
    content = json.load(file)


class PriseKm:
    def __init__(self, content: dict) -> list:
        self.content = content

    def distens_prise() -> dict:
        global customers
        customers = content.get("customers")
        global prise_fuel
        prise_fuel = content.get("FUEL_PRICE")
        dict_prise_ = []
        for customer_n in customers:
            coordinates_customer = customer_n.get("location")
            fuel_consumption_car2 = (
                customer_n.get("car").get("fuel_consumption")
            )
            for vel in Shop.shop1_location_shop1():
                coordinates_shop = Shop.shop1_location_shop1().get(vel)
                distens_custom_x = coordinates_customer[0]
                distens_custom_y = coordinates_customer[1]
                distens_location_shop_x = coordinates_shop[0]
                distens_location_shop_y = coordinates_shop[1]
                distens = (
                    math.sqrt((distens_custom_x
                               - distens_location_shop_x) ** 2
                              + (distens_custom_y
                                 - distens_location_shop_y) ** 2)
                )
                prise_distens = (
                    (distens
                        * 2 / 100)
                    * fuel_consumption_car2
                    * prise_fuel
                )
                prise_distens = round(prise_distens, 2)
                dict_prise_.append(prise_distens)
        return dict_prise_
