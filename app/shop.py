from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def cost_food(self, customer: callable) -> float:
        cost_food = 0
        for food in customer.product_cart.keys():
            cost_food += customer.product_cart[food] * self.products[food]
        return cost_food
