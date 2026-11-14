import datetime
from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict[str, float]

    def has_products(self, product_cart: dict) -> bool:
        return all(product in self.products for product in product_cart)

    def calculate_products_cost(self, product_cart: dict) -> tuple:
        product_costs = {
            product: self.products[product] * count
            for product, count in product_cart.items()
        }
        total_cost = sum(product_costs.values())
        return product_costs, total_cost

    def print_receipt(
        self,
        product_cart: dict,
        product_costs: dict,
        total_cost: float,
        customer_name: str,
    ) -> None:
        print(f"Date: {datetime.datetime.now():%d/%m/%Y %H:%M:%S}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, count in product_cart.items():
            print(f"{count} {product}s for {product_costs[product]:g} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
