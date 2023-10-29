from math import dist
from typing import Dict, Any

from app.car import Car


class Customer:
    def __init__(self, customer_data: Dict[str, Any]) -> None:
        self.name = customer_data["name"]
        self.product_cart = customer_data["product_cart"]
        self.location = customer_data["location"]
        self.money = customer_data["money"]
        self.car = Car(customer_data["car"])
        self.home_location = customer_data["location"]
        self.__cheapest_shop = None
        self.__possible_shops = None

    def __calculate_purchase_price_for_each_shop(self, shops: list) -> None:
        self.__possible_shops = {}

        for shop in shops:
            purchase_price = 0
            for product, amount in self.product_cart.items():
                purchase_price += shop.products[product] * amount

            self.__possible_shops[shop] = {"purchase_price": purchase_price}

    def __calculate_fuel_cost_to_each_shop(self, fuel_price: float) -> None:
        for shop in self.__possible_shops:
            distance_to_shop = dist(shop.location, self.location)
            roundtrip_cost = ((distance_to_shop * 2)
                              * (self.car.fuel_consumption / 100)
                              * fuel_price)

            self.__possible_shops[shop]["roundtrip_cost"] = roundtrip_cost

    def calculate_total_trip_cost_for_each_shop(self,
                                                shops: list,
                                                fuel_price: float) -> None:
        self.__calculate_purchase_price_for_each_shop(shops)
        self.__calculate_fuel_cost_to_each_shop(fuel_price)

        self.__possible_shops = {
            shop: round(
                sum(
                    (self.__possible_shops[shop]["purchase_price"],
                     self.__possible_shops[shop]["roundtrip_cost"])
                ), 2
            )
            for shop
            in self.__possible_shops
        }
        return self.__possible_shops

    def choose_cheapest_shop(self) -> dict:
        cheapest_shop_data = min(
            self.__possible_shops.items(), key=lambda item: item[1]
        )
        self.__cheapest_shop = {
            "shop": cheapest_shop_data[0], "total_cost": cheapest_shop_data[1]
        }
        return self.__cheapest_shop

    def evaluate_shopping_possibility(self) -> bool:
        return self.__cheapest_shop["total_cost"] <= self.money

    def go_to_the_shop(self) -> None:
        self.location = self.__cheapest_shop["shop"].location

    def go_home(self) -> None:
        self.location = self.home_location

    def calculate_rest_of_money(self) -> float:
        return self.money - self.__cheapest_shop["total_cost"]
