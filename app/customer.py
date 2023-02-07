import json
import math

from shops import Shops


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

    def cost_trip(self, market):
        distance_to_market = self.distance_two_points(market.location, self.location)
        fuel_cost = 2 * distance_to_market * self.car["fuel_consumption"] / 100 * fuel_price
        money_in_market = Shops.get_total(market, self)
        total_cost = round((money_in_market + fuel_cost), 2)
        return total_cost




if __name__ == "__main__":
    with open("config.json", "r") as data_file:
        config_file = json.load(data_file)
        fuel_price = config_file["FUEL_PRICE"]

        for shop in config_file["shops"]:
            market = Shops(shop)
        for customer in config_file["customers"]:
            person = Customers(customer)
                    #-----START-----#
            print(f"{person.name} has {person.money} dollars")
            dict_cost = {}
            for shop in market.list_of_shops:
                cost_trip = person.cost_trip(shop)
                print(f"{person.name}'s trip to the {shop.name} costs {cost_trip}")
                dict_cost[shop.name] = cost_trip
            min_money = min(dict_cost.values())
            for key, value in dict_cost.items():
                if value == min_money:
                    favorite_shop = key
                    print(f"{person.name} rides to {favorite_shop}\n")
            for shop in market.list_of_shops:
                if shop.name == favorite_shop:
                    print(shop.name)
                    Shops.print_receipt(shop, person)