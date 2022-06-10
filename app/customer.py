import math

from app.car import GasStation, Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 products_cart: dict,
                 location: list,
                 money: int,
                 car: Car):
        self.name = name
        self.products_card = products_cart
        self.location = location
        self.money = money
        self.car = car

    def dist_to(self, other_obj: Shop):
        return math.dist(self.location, other_obj.location)

    def cost_fuel(self,
                  shop: Shop,
                  station: GasStation):
        fuel_for_one_km = station.fuel_price * self.car.fuel_consumption / 100
        return fuel_for_one_km * self.dist_to(shop)

    def coast_prod_cart(self, shop: Shop):
        self.total_amount = 0
        for prod in self.products_card:
            if prod in shop.products:
                self.total_amount += \
                    (self.products_card[prod] * shop.products[prod])
        return self.total_amount

    def total_cost_trip(self,
                        shop: Shop,
                        gas_station: GasStation):
        total_cost_on_fuel = 2 * self.cost_fuel(shop, gas_station)
        self.total_cost = self.coast_prod_cart(shop) + total_cost_on_fuel
        return round(self.total_cost, 2)

    def change_location(self, new_location_cords: list):
        self.location = new_location_cords

    def to_buy(self, amount):
        self.money -= amount

    def go_to_shop(self, shop: Shop):
        print(f"{self.name} rides to {shop.name}")

    def check_money(self):
        print(f"{self.name} now has {self.money} dollars\n")
