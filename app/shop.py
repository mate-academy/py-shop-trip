import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(
        self, name: str, location: list[float], products: dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def purchase_cost(self, product_cart: dict[str, int]) -> float | None:
        if any(product not in self.products for product in product_cart):
            return None
        return sum(
            quantity * self.products[product]
            for product, quantity in product_cart.items()
        )

    def sell_products(self, customer: Customer) -> None:
        total = self.purchase_cost(customer.product_cart)
        if total is None:
            return

        print(f"Date: {datetime.datetime.now():%d/%m/%Y %H:%M:%S}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in customer.product_cart.items():
            price = quantity * self.products[product]
            print(f"{quantity} {product}s for {price:g} dollars")
        print(f"Total cost is {total:g} dollars")
        print("See you again!")
        customer.money -= total
