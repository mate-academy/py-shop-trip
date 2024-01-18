from math import sqrt


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_distance(self, customer_location: list) -> float:
        distance = sqrt(
            (self.location[0] - customer_location[0]) ** 2 +
            + (self.location[1] - customer_location[1]) ** 2
        )
        return distance

    def products_cost(self, product_cart: dict) -> float:
        cost = cost = sum(
            self.products[key] * value for key, value in product_cart.items()
        )

        return cost
