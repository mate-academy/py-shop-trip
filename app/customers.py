import math


class Customer:
    def __init__(self, user_info, fuel_price):
        self.name = user_info["name"]
        self.product_cart = user_info["product_cart"]
        self.location = user_info["location"]
        self.money = user_info["money"]
        self.car = user_info["car"]
        self.fuel_price = fuel_price

    def fuel_costs(self, shop):
        distance = math.dist(shop.location, self.location)
        return self.fuel_price * distance * self.car["fuel_consumption"] / 100

    def pay_for_trip(self, amount):
        self.money -= amount
        return self.money

    def products_costs(self, shop):
        return sum(
            amount * shop.products[product]
            for product, amount in self.product_cart.items()
        )

    def trip_costs(self, shop):
        return round(2 * self.fuel_costs(shop) + self.products_costs(shop), 2)
