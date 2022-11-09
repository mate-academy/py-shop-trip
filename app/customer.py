from math import dist
from app.shop import Shop


class Customer:
    def __init__(self, customer: dict) -> None:
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.car = customer["car"]

    def calculate_distance_to_shop(self, shop: Shop) -> float:
        return dist(self.location, shop.location)

    def cost_of_products(self, shop: Shop) -> dict:
        return {
            shop.name: {
                key: (value * self.product_cart[key])
                for key, value in shop.products.items()
            }
        }

    def product_price(self, shop: Shop) -> dict:
        return {
            shop: sum(products.values())
            for shop, products in self.cost_of_products(shop).items()
        }
