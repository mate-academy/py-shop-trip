import math
from app.car import Car


class Customer:
    def __init__(self, name, product_cart, location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car['brand'], car['fuel_consumption'])

    def distance_to(self, shop_location):
        return math.sqrt((self.location[0] - shop_location[0]) ** 2 + (self.location[1] - shop_location[1]) ** 2)

    def calculate_trip_total(self, shop, fuel_price):
        distance_to_shop = self.distance_to(shop.location)
        fuel_cost = self.car.calculate_trip_cost(distance_to_shop * 2, fuel_price)  # Round trip cost
        product_cost = shop.calculate_total_cost(self.product_cart)
        return fuel_cost + product_cost, fuel_cost, product_cost

    def go_shopping(self, shop, fuel_cost, product_cost):
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location
        self.money -= fuel_cost + product_cost
        shop.print_receipt(self.name, self.product_cart, product_cost)
        self.location = [0, 0]  # Assume home location is at [0, 0]
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money:.2f} dollars\n")
