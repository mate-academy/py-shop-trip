from dataclasses import dataclass


@dataclass
class Shop:

    @staticmethod
    def cost_all_products(products: dict, product_cart: dict) -> float:
        result = 0
        for product in product_cart:
            result += product_cart[product] * products[product]
        return result
