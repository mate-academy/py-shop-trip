# flake8: noqa E231
import datetime
import math
from dataclasses import dataclass

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    products: dict
    location: [int, int]
    money: int | float
    car: Car

    def cart_cost(self, shop: Shop) -> int | float:
        cart_cost = 0
        for product, quantity in self.products.items():
            if product in shop.products:
                cart_cost += quantity * shop.products[product]
        return cart_cost

    def fuel_cost(
            self,
            fuel_price: int | float,
            distance: int | float
    ) -> int | float:
        cost = self.car.vol_of_fuel / 100 * distance * fuel_price
        return cost

    def calculate_trip_cost(
            self,
            shop: Shop,
            fuel_price: int | float
    ) -> int | float:
        distance = self.calculate_distance(shop)
        fuel_cost = self.fuel_cost(fuel_price, distance)
        cart = self.cart_cost(shop)
        trip_cost = fuel_cost * 2 + cart
        return round(trip_cost, 2)

    def calculate_distance(self, shop: Shop) -> int | float:
        distance = math.dist(shop.location, self.location)
        return distance

    def cheapest_shopping(
            self,
            shops: [Shop],
            fuel_price: int | float
    ) -> Shop:
        print(f"{self.name} has {self.money} dollars")
        trip_costs = []
        for shop in shops:
            trip_cost = self.calculate_trip_cost(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")
            trip_costs.append(trip_cost)
        min_cost = min(trip_costs)
        index = trip_costs.index(min_cost)
        return shops[index]

    def shopping(self, shop: Shop, fuel_price: int | float) -> None:
        self.money -= self.calculate_trip_cost(shop, fuel_price)
        self.location = shop.location
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%d/%m/%Y %H:%M:%S")

        print(
            f"Date: {formatted_time}\n"
            f"Thanks, {self.name}, for your purchase!\n"
            f"You have bought:")
        for product, quantity in self.products.items():
            if product in shop.products:
                value = quantity * shop.products[product]
                if value == int(value):
                    value = round(value)
                print(f"{quantity} {product}s for {value} dollars")
        print(
            f"Total cost is {self.cart_cost(shop)} dollars\n"
            f"See you again!\n"
        )

        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")
