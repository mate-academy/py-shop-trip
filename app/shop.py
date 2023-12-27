from __future__ import annotations
from typing import List, Dict
from dataclasses import dataclass
from app.customers import Customers


@dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict[str, float]

    @classmethod
    def get_shops(cls, shop_data: List[Dict[str | Customers]]) -> list[Shop]:
        shops = []
        for data in shop_data:
            shop = cls(
                name=data["name"],
                location=data["location"],
                products=data["products"]
            )
            shops.append(shop)
        return shops

    def purchase(self, customer: Customers, date: str) -> str:
        purchased_items = []
        total_cost = 0

        for product, quantity in customer.product_cart.items():
            if product in self.products:
                product_price = self.products[product]
                cost = product_price * quantity
                purchased_items.append((product, quantity, cost))
                total_cost += cost

        receipt = f"Date: {date}\n"
        receipt += f"Thanks, {customer.name}, for your purchase!\n"
        receipt += "You have bought:\n"
        for item, quantity, cost in purchased_items:
            if cost % 1 == 0:
                receipt += f"{quantity} {item}s for {int(cost)} dollars\n"
            else:
                receipt += f"{quantity} {item}s for {round(cost, 2)} dollars\n"
        receipt += f"Total cost is {total_cost} dollars\n"
        receipt += "See you again!"

        return receipt
