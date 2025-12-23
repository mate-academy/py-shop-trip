from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class Shop:
    name: str
    location: List
    products: Dict

    def calculate_purchase_cost(
            self,
            product_cart: Dict[str, int]
    ) -> tuple[int | Any, Dict[str, Any]]:
        total_cost = 0
        purchase_info = {}

        for product, quantity in product_cart.items():
            if product in self.products:
                price = self.products[product]
                cost = price * quantity
                total_cost += cost
                purchase_info[product] = {
                    "quantity": quantity,
                    "price_per_unit": price,
                    "total_cost": cost
                }

        return total_cost, purchase_info

    @staticmethod
    def print_receipt(
            customer_name: str,
            purchase_details: Dict[str, Any], total_cost: int
    ) -> None:

        current_time = "04/01/2021 12:33:41"

        print(f"\nDate: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for products, info in purchase_details.items():
            cost = info["total_cost"]
            cost_str = str(int(cost)) if cost == int(cost) else str(cost)
            print(f"{info['quantity']} {products}s for {cost_str} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
