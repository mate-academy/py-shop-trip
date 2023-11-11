from typing import Dict, List


class Shop:
    def __init__(
            self,
            name: str,
            location: Dict,
            product_cart: List,
            fuel_price: float
    ) -> None:
        self.name = name
        self.location = location
        self.product_cart = product_cart
        self.fuel_price = fuel_price

    def shopping_cost(self, product_cart: List) -> float:
        total_cost = sum(self.product_cart[product] * product_cart[product]
                         for product in product_cart.keys())
        return round(total_cost, 2)

    def generate_receipt(
            self,
            customer: str,
            current_time: str,
            fuel_price: float
    ) -> str:
        receipt = f"Date: {current_time}\nThanks, {customer.name}," \
                  f" for your purchase!\nYou have bought:\n"
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            if product in self.product_cart:
                product_cost = self.product_cart[product]
                product_total_cost = float(product_cost * quantity)
                if product_total_cost.is_integer():
                    product_total_cost = int(product_total_cost)
                receipt += (
                    f"{quantity} {product}s for "
                    f"{product_total_cost} dollars"
                )
                total_cost += product_total_cost
        receipt += f"\nTotal cost is {total_cost} dollars\nSee " \
                   f"you again!\n\n{customer.name} rides home"
        return receipt
