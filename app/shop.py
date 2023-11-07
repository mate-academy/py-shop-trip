from dataclasses import dataclass
from datetime import datetime
from typing import List

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: List[int]
    products: dict

    def calculate_product_cost(
            self,
            customer: Customer,
    ) -> dict:
        """Returns dict with purchases as product: [amount, cost per amount]"""
        purchases = {
            "milk": [],
            "bread": [],
            "butter": []
        }
        for item in purchases.keys():
            amount = customer.products_cart.get(item, 0)
            price = self.products.get(item, 0)
            cost_per_amount = amount * price
            purchases[item] = [amount, cost_per_amount]

        return purchases

    @staticmethod
    def calculate_trip_cost(
            purchases: dict,
            fuel_expenses: float
    ) -> float:
        """Returns cost of whole trip and shopping"""
        return sum(cost[1] for cost in purchases.values()) + fuel_expenses * 2

    @staticmethod
    def generate_receipt(
            customer: Customer,
            purchased_products: dict
    ) -> None:
        """Generates and prints receipt"""
        print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              "You have bought: ")
        total = 0
        for product, (amount, cost) in purchased_products.items():
            if int(cost) == cost:
                cost = int(cost)
            print(f"{amount} {product}s for {cost} dollars")
            total += cost
        print(f"Total cost is {round(total, 2)} dollars"
              f"\nSee you again!""")
