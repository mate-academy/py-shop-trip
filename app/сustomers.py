import math
class Customers:
    def __init__(self,name, product_cart: dict, location, money, car: dict):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def ride_to_shop(self, coord_s):
        self.home = self.location
        self.location = coord_s

    def ride_home(self):
        self.location = self.home

    def calculate_products(self, list_shops):
        calculated_list = {}
        for name, shop in list_shops.items():
            for product in self.product_cart:
                if product in shop.products:
                    calculated_list[name] = {product: shop.products[product] * self.product_cart[product] for
                                             product in shop.products}
        return calculated_list

    def calculate_road(self, list_shops, fuel):
        calculated_list = {}
        for name, shop in list_shops.items():
            calculated_list[name] = (((self.distance(shop.location) * 2) / 100) * self.car["fuel_consumption"]) * fuel
        return calculated_list

    def distance(self, shop_location):
        return math.sqrt((shop_location[0] - self.location[0]) ** 2 + (shop_location[1] - self.location[1]) ** 2)

def create_customers(list_customers):
    customers ={}
    for customer in list_customers:
        customers[customer["name"]] = Customers(customer["name"], customer["product_cart"], customer["location"],customer["money"], customer["car"])
    return customers

def total(products, road):
    total = {}
    for name, value in products.items():
        total[name] = round((sum(value.values()) + road[name]), 2)
    return total

