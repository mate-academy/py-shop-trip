from decimal import Decimal
from app.shop import Shop


class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list,
                 money: Decimal) -> None:

        self.name = name
        self.product_cart = product_cart
        self.location = [Decimal(str(loc)) for loc in location]
        self.money = Decimal(str(money))

    def check_price_products(self, shop: Shop) -> Decimal:
        return sum([shop.products[product] * self.product_cart[product]
                    for product in self.product_cart.keys()])
