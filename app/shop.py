from dataclasses import dataclass


@dataclass
class Shop:
    product_shop: dict
    product_cart: dict

    def get_cheapest_shop(self) -> float:
        amount = 0

        for key_cart, value_cart in self.product_cart.items():
            if key_cart in self.product_shop:
                amount += value_cart * self.product_shop[key_cart]
        return round(amount, 2)
