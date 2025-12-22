import math
from app.car import Car

class Customer:

    def __init__(self, name, product_cart, current_location, money, car, home):
        self.name = name
        self.product_cart = product_cart
        self.current_location = current_location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])
        self.home = home
    
    def calculate_distance_to(self, shop_location):
        x1, y1 = self.current_location
        x2, y2 = shop_location
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance
    
    def calculate_products_cost(self, shop):
        products_cost = 0
        for product_name, quantity in self.product_cart.items():
            products_cost += shop.calculate_product_cost(product_name, quantity)
        return products_cost
    
    def calculate_trip_cost(self, shop, fuel_price):
        distance_to_shop = self.calculate_distance_to(shop.location)
        total_distance = distance_to_shop * 2
        _, total_fuel_cost = self.car.calculate_fuel_needed(total_distance, fuel_price)
        product_cost = self.calculate_products_cost(shop)
        total_cost = total_fuel_cost + product_cost
        return total_cost
    
    def find_cheapest_shop(self, shops, fuel_price):
        cheapest_shop = None
        cheapest_cost = float('inf')
        for shop in shops:
            cost = self.calculate_trip_cost(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs {cost:.2f}")
            if cost < cheapest_cost:
                cheapest_cost = cost
                cheapest_shop = shop
        return cheapest_shop, cheapest_cost
    
    def travel_to(self, shop):
        print(f"{self.name} rides to {shop.name}")
        self.current_location = shop.location
    
    def purchase(self, shop, total_trip_cost):
        shop.print_receipt(self.name, self.product_cart)
        self.money -= total_trip_cost
    
    def go_home(self):
        print(f"{self.name} rides home")
        self.current_location = self.home