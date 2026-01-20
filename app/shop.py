from app.customer import Customer
from datetime import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def products_cost(self, customer: Customer) -> float:
        product_cart = customer.product_cart
        product_cost = 0
        for product, qty in product_cart.items():
            product_cost += qty * self.products.get(product)
        return product_cost

    def print_check(self, customer: Customer) -> None:
        current_datatime = datetime(2021, 1, 4, 12, 33, 41)
        current_datatime = current_datatime.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_datatime}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in customer.product_cart.items():
            if product in self.products:
                cost = self.products[product] * quantity
                cost_str = f"{cost:.1f}" if cost % 1 else f"{int(cost)}"
                print(f"{quantity} {product}s for {cost_str} dollars")
        print(f"Total cost is {self.products_cost(customer)} dollars")
        print("See you again!\n")
