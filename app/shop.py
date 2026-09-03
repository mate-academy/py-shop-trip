import math


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict[str, float | int],
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @classmethod
    def create_shop_from_dict(cls, shop_dict: dict) -> Shop:
        return Shop(
            name=shop_dict["name"],
            location=shop_dict["location"],
            products=shop_dict["products"]
        )

    def calculate_product_cart_price(self, product_cart: dict) -> float | int:
        result = 0
        for key, value in product_cart.items():
            result += product_cart[key] * self.products[key]
        return result

    def distance_from_customer(self, customer_location: list) -> float | int:
        return math.dist(self.location, customer_location)
