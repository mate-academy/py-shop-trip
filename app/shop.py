from dataclasses import dataclass
from typing import Dict, List
from datetime import datetime


@dataclass
class Shop:
    name: str
    location: List[int]  # [x, y]
    products: Dict[str, float]  # название -> цена

    def calculate_cart_price(self, cart: Dict[str, int]) -> float:
        """Посчитать стоимость корзины товаров в этом магазине."""
        total = 0.0
        for product, quantity in cart.items():
            price = self.products.get(product)
            if price is None:
                raise ValueError(f"{self.name} не продаёт {product}")
            total += price * quantity
        return total

    def print_receipt(self, customer_name: str, cart: Dict[str, int]) -> None:
        """Вывод чека после покупки."""
        print(f"\nDate: {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total = 0.0
        for product, qty in cart.items():
            cost = self.products[product] * qty
            total += cost
            print(f"{qty} {product}s for {cost} dollars")
        print(f"Total cost is {round(total, 2)} dollars")
        print("See you again!")
