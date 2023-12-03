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
        purchase_price = 0
        for product, quantity in client.product_cart.items():
            if product in self.products:
                price_per_unit = self.products[product]
                cost = price_per_unit * quantity
                if int(cost) == cost:
                    cost = int(cost)
                purchase_price += cost
                print(f"{quantity} {product}s for {round(cost, 1)} dollars")
        return purchase_price
