import json
import math

from app.shops import Shops


class Customers:
    def __init__(self, customer_dict: dict) -> None:
        self.name = customer_dict["name"]
        self.prod_cart = customer_dict["product_cart"]
        self.location = customer_dict["location"]
        self.money = customer_dict["money"]
        self.car = customer_dict["car"]

    @staticmethod
    def distance_two_points(point_1: list, point_2: list):
        x1, y1 = point_1
        x2, y2 = point_2
        return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)

    def calc_trip(self, market: Shops):
        with open("app.config.json", "r") as config:
            data_file = json.load(config)
            distance_to_shops = {shop["name"]: self.distance_two_points(shop["location"], self.location)
                                 for shop in data_file["shops"]}
            name_of_nearest_shop = min(distance_to_shops, key=lambda unit: distance_to_shops[unit])
            fuel_cost = 2 * data_file["shops"][name_of_nearest_shop] * data_file[
                "FUEL_PRICE"] * self.car["fuel_consumption"] / 100
        return fuel_cost + Shops.get_total(data_file["shops"][name_of_nearest_shop].__name__, self)

