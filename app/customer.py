from app.shop import Shop


class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list[int],
                 money: int) -> None:

        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money

    def check_price_products(self, shop: Shop) -> bool:
        return sum([shop.products[product] * self.product_cart[product]
                    for product in self.product_cart.keys()])
