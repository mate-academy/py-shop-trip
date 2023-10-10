import math
from app.car import Car


class Customer:
    FUEL_PRICE = 2.4

    def __init__(self, data):
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car = Car(data["car"])

    def calculate_trip_cost(self, shop):
        distance_to_shop = self.calculate_distance(shop.location)
        fuel_consumption_per_km = self.car.fuel_consumption / 100
        fuel_cost_to_shop = (distance_to_shop * fuel_consumption_per_km) * self.FUEL_PRICE
        product_cost = sum([self.product_cart[product] * shop.products[product] for product in self.product_cart])
        total_trip_cost = fuel_cost_to_shop + product_cost
        return round(total_trip_cost, 2)

    def has_enough_money(self, trip_cost):
        return self.money >= trip_cost

    def travel_to_shop(self, shop):
        self.location = shop.location
        print(f"{self.name} rides to {shop.name}\n")

    def travel_home(self, trip_cost):
        print(f"{self.name} rides home\n")
        remaining_money = self.money - trip_cost
        print(f"{self.name} now has {round(remaining_money, 2)} dollars\n")

    def calculate_distance(self, shop_location):
        x_location = self.location[0] - shop_location[0]
        y_location = self.location[1] - shop_location[1]
        distance = math.sqrt(x_location ** 2 + y_location ** 2)
        return distance
