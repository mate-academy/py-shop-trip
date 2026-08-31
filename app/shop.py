from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict[str, int],
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def cost_products(self, customer: Customer) -> int | float:
        return sum(
            amount
            * self.products[product]
            for product, amount in customer.product_cart.items()
        )
