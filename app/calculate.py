import math
from app.сustomers import Customers


class Calculate:
    def __init__(self, customer: Customers, shops: dict) -> None:
        self.customer = customer
        self.shops = shops

    def calculate_products(self, shops: dict) -> dict:
        calculated_list = {}
        for name, shop in shops.items():
            for product in self.customer.product_cart:
                if product in shop.products:
                    calculated_list[name] = {
                        item: shop.products[item]
                        * self.customer.product_cart[item]
                        for item in shop.products
                    }
        return calculated_list

    def calculate_road(self, shops: dict, fuel: int) -> dict:
        calculated_list = {}
        for name, shop in shops.items():
            road = self.distance(shop.location)
            calculated_list[name] = ((((road * 2) / 100)
                                     * self.customer.car["fuel_consumption"])
                                     * fuel)
        return calculated_list

    def distance(self, shop_location: list) -> float:
        return math.sqrt((shop_location[0]
                          - self.customer.location[0]) ** 2
                         + (shop_location[1]
                            - self.customer.location[1]) ** 2)

    def total(self, products: dict, road: dict) -> dict:
        total = {}
        for name, value in products.items():
            total[name] = round((sum(value.values()) + road[name]), 2)
        return total
