import math


class Customer:
    def __init__(self, name, product_cart, location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.location = location[:]
        self.money = money
        self.car = car
        self.home_location = location[:]

    def distance_to(self, location):
        """count distance between customer and location"""
        return math.sqrt((self.location[0] - location[0]) ** 2 +
                         (self.location[1] - location[1]) ** 2)

    def count_total_trip_cost(self, shop, fuel_price):
        """count total trip cost"""
        distance = self.distance_to(shop.location)
        trip_cost = 2 * self.car.calculate_fuel_cost(distance, fuel_price)
        product_cost = shop.calculate_products_cost(self.product_cart)
        if product_cost is None:
            return None
        return trip_cost + product_cost

    def go_home(self):
        print(f"{self.name} rides home")
        self.location = self.home_location[:]

    def buy_products(self, shop, fuel_cost):
        total_trip_cost = self.count_total_trip_cost(shop, fuel_cost)

        if total_trip_cost is None:
            print(f"{self.name} can't buy all products in {shop.name}")
            return
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location[:]
        shop.print_receipt(self)
        self.money -= total_trip_cost
        self.go_home()
