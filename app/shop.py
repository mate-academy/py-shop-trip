from math import sqrt


class Shop:
    def __init__(self, name: str, location: list, products: list) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_distance(self,
                     customer_location: list,
                     shop_location: list) -> float:
        x1, y1 = customer_location
        x2, y2 = shop_location
        distance = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2))

        return distance

    def get_product_cost(self, product_cart: dict) -> float:
        product_cost = sum(
            [self.products[product] * quantity for product, quantity
             in product_cart.items() if product in self.products]
        )

        return product_cost
