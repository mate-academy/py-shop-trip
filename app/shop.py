class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict[str, int]
    ) -> None:

        self.name = name
        self.location = location
        self.products = products

    def cart_cost_calculation(
            self,
            product_cart: dict[str, int]
    ) -> float | int:

        result = 0

        for key, value in product_cart.items():
            if key in self.products:
                result += round(value * self.products[key], 2)

        return result
