import math

from app.car import GasStation, Car
from app.shop import Shop


class Customer:
    fuel_price = GasStation(2.4)

    def __init__(self, name: str, products_cart: dict, location: list, money: int, car: Car):
        self.name = name
        self.products_card = products_cart
        self.location = location
        self.money = money
        self.car = car

    def calc_distance_to(self, other_obj: Shop):
        return math.dist(self.location, other_obj.location)

    def calc_cost_fuel_for_go_to_shop(self, shop: Shop):
        return self.fuel_price.fuel_price * self.calc_distance_to(shop) * self.car.fuel_consumption / 100

    def calc_coast_for_all_in_product_cart(self, shop: Shop):
        self.total_amount_in_shop = 0
        for product in self.products_card:
            if product in shop.products:
                self.total_amount_in_shop += (self.products_card[product] * shop.products[product])
        return self.total_amount_in_shop

    def calc_total_amount_cost_for_trip_to_shop(self, shop: Shop):

        self.total_amount_for_trip = self.calc_coast_for_all_in_product_cart(shop) + 2 * self.calc_cost_fuel_for_go_to_shop(shop)
        return round(self.total_amount_for_trip, 2)

    def change_location(self, new_location_coords: list):
        self.location = new_location_coords

    def to_buy(self, amount):
        self.money -= amount

    def go_to_shop(self, shop: Shop):
        print(f"{self.name} rides to {shop.name}")

    def check_money(self):
        print(f"{self.name} now has {self.money} dollars\n")
