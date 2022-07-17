import math


class Client:
    def __init__(self, name,
                 product_cart,
                 location,
                 money,
                 car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def price_at_road(self, fuel_price, shop):
        kilometers = \
            math.sqrt(
                (self.location[0] - shop.location[0]) ** 2 +
                (self.location[1] - shop.location[1]) ** 2)
        price_road = (self.car.fuel_consumption / 100) * fuel_price
        return price_road * kilometers

    def shopping(self, shop):
        sum_purchase = 0
        for product, amount in self.product_cart.items():
            sum_purchase += amount * shop.products[product]
        return sum_purchase

    def __repr__(self):
        return f"Name {self.name}"
