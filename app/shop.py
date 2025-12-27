from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    cost_products: dict

    def get_cost_products(self, product_cart: dict) -> float:
        cost_products = 0
        for product in product_cart:
            cost_products += (product_cart[product]
                              * self.cost_products[product])
        return cost_products
