from math import sqrt
import datetime

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, data: dict, fuel_price: float) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.home_location = list(self.location)
        self.money = data["money"]
        self.car = Car(data["car"]["brand"], data["car"]["fuel_consumption"])
        self.fuel_price = fuel_price

    def distance_to(self, shop_location: list) -> float:
        return sqrt(
            (self.location[0] - shop_location[0]) ** 2
            + (self.location[1] - shop_location[1]) ** 2
        )

    def fuel_cost_for_distance(self, distance: float) -> float:
        return (distance / 100) * self.car.fuel_consumption * self.fuel_price

    def total_trip_cost(self, shop: Shop) -> float:
        distance = self.distance_to(shop.location)
        fuel_cost = self.fuel_cost_for_distance(distance * 2)
        product_cost = shop.calculate_cart_total(self.product_cart)
        return round(fuel_cost + product_cost, 2)

    def can_afford_trip(self, shop: Shop) -> tuple:
        if not shop.has_all_products(self.product_cart):
            return False, float("inf")
        total_cost = self.total_trip_cost(shop)
        return total_cost <= self.money, total_cost

    def travel_to(self, location: list) -> None:
        self.location = location

    def return_home(self) -> None:
        self.location = self.home_location

    def buy_from(self, shop: Shop) -> None:
        distance = self.distance_to(shop.location)
        fuel_cost = self.fuel_cost_for_distance(distance * 2)
        product_cost = shop.calculate_cart_total(self.product_cart)
        total_cost = fuel_cost + product_cost

        self.travel_to(shop.location)
        print(f"{self.name} rides to {shop.name}")
        print()

        print("Date:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in self.product_cart.items():
            price = shop.products[product]
            cost = quantity * price
            if cost.is_integer():
                cost_str = str(int(cost))
            else:
                cost_str = str(cost)
            print(f"{quantity} {product}s for {cost_str} dollars")
        if product_cost.is_integer():
            total_str = str(int(product_cost))
        else:
            total_str = str(round(product_cost, 2))
        print(f"Total cost is {total_str} dollars")
        print("See you again!")

        print()
        self.return_home()
        print(f"{self.name} rides home")
        self.money -= total_cost
        self.money = round(self.money, 2)
        if self.money.is_integer():
            money_str = str(int(self.money))
        else:
            money_str = str(round(self.money, 2))
        print(f"{self.name} now has {money_str} dollars")
        print()
