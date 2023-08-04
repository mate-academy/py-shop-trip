class Customer:
    def __init__(self, name, product_cart, location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip_cost(self, shop, fuel_price):
        distance_to_shop = self.calculate_distance(shop.location)
        fuel_cost_to_shop = self.car.fuel_cost(distance_to_shop, fuel_price)
        total_product_cost = self.calculate_product_cost(shop.products)
        total_trip_cost = 2*fuel_cost_to_shop + total_product_cost
        return round(total_trip_cost, 2)

    def calculate_distance(self, destination_location):
        x1, y1 = self.location
        x2, y2 = destination_location
        return round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 2)

    def calculate_product_cost(self, shop_products):
        total_cost = 0
        for product, quantity in self.product_cart.items():
            if product in shop_products:
                total_cost += shop_products[product] * quantity
        return round(total_cost, 2)

    def update_money(self, amount):
        self.money -= amount