from math import dist
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: dist
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def __repr__(self) -> str:
        return f"name({self.name}), " \
               f"location({self.location}), " \
               f"money({self.money})"

    def cost_products(self, shop: Shop) -> dict:
        return {
            shop.name: {
                key: (value * self.product_cart[key])
                for key, value in shop.products.items()
            }
        }

    def product_price(self, shop: Shop) -> dict:
        return {
            shop: sum(products.values())
            for shop, products in self.cost_products(shop).items()
        }

    def distance_to_shop(self, shop: Shop) -> float:
        return dist(self.location, shop.location)
