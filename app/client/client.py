
import math


class Client:

    def __init__(self, name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def price_for_road(self, fuel_price, shop):
        kilometers = \
            math.sqrt(
                (self.location[0] - shop.location[0]) ** 2 +
                (self.location[1] - shop.location[1]) ** 2)
        cost_road = (self.car.fuel_consumption / 100) * fuel_price
        return cost_road * kilometers

    def purchase_at_shop(self, shop):
        sum_buy = 0
        for product, amount in self.product_cart.items():
            sum_buy += amount * shop.products[product]
        return sum_buy

    def __repr__(self):
        return f"Name {self.name}"
