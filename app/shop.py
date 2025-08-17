import datetime
from typing import Dict, Tuple
from app.customer import Customer  # імпорт класу Customer

class Shop:
    def __init__(self, name: str, location: Tuple[int, int], products: Dict[str, float]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def has_all_products(self, cart: Dict[str, int]) -> bool:
        """Перевіряє, чи є всі продукти з кошика у магазині"""
        return all(product in self.products for product in cart)

    def print_receipt(self, customer: Customer, fuel_price: float) -> None:
        """Друкує чек покупки для клієнта"""
        now = datetime.datetime.now()
        print(f"Date: {now.strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total = 0.0
        for product, quantity in customer.product_cart.items():
            if product in self.products:
                cost = self.products[product] * quantity
                total += cost
                print(
                    f"{quantity} {product}s for {cost:.2f} dollars"
                )

        print(f"Total cost is {total:.2f} dollars")
        print("See you again!\n")
