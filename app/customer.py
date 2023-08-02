class Customer:
    def __init__(self, name, product_cart, location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip_cost(self, shop, fuel_price):
        distance_to_shop = self.calculate_distance(shop)
        fuel_cost_to_shop = self.car.get_fuel_cost(distance_to_shop, fuel_price)
        total_product_cost = self.calculate_product_cost(shop.products)
        distance_back_home = self.calculate_distance_home(shop)
        fuel_cost_back_home = self.car.get_fuel_cost(distance_back_home, fuel_price)
        return fuel_cost_to_shop + total_product_cost + fuel_cost_back_home

    def calculate_distance(self, destination):
        return ((destination.location[0] - self.location[0]) ** 2 + (destination.location[1] - self.location[1]) ** 2) ** 0.5

    def calculate_distance_home(self, destination):
        home_location = [0, 0]
        return ((destination.location[0] - home_location[0]) ** 2 + (destination.location[1] - home_location[1]) ** 2) ** 0.5

    def calculate_product_cost(self, shop_products):
        total_cost = 0
        for product, quantity in self.product_cart.items():
            if product in shop_products:
                total_cost += shop_products[product] * quantity
        return total_cost
