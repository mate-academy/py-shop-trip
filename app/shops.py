from typing import Type


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

    def process_purchase(self, client: Type) -> None:
        print("You have bought: ")

        for product, quantity in client.product_cart.items():
            if product in self.products:
                price_per_unit = self.products[product]
                cost = price_per_unit * quantity
                print(f"{quantity} {product}s for {cost} dollars")
