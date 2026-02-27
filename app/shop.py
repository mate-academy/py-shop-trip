from dataclasses import dataclass
from typing import Dict
import datetime
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: tuple[int, int]
    products: Dict[str, int | float]

    def calc_groceries_cost(self, customer: "Customer") -> float:
        cost = 0.0
        for product, quantity in customer.products.items():
            if product in self.products:
                cost += self.products[product] * quantity
        return cost

    def print_recipe(self, customer: "Customer") -> None:
        cost = self.calc_groceries_cost(customer)
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in customer.products.items():
            if product in self.products:
                product_cost = self.products[product] * quantity
                print(f"{quantity} {product}s for {product_cost:g} dollars")

        print(f"Total cost is {cost:g} dollars")
        print("See you again!\n")
