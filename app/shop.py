from dataclasses import dataclass
import datetime

from app.location import Location
from app.customer import Customer


@dataclass
class Shop:
    _name: str
    _location: Location
    _products: dict

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> Location:
        return self._location

    @property
    def products(self) -> dict:
        return self._products

    def calculate_cart_cost(self, product_cart: dict) -> float | int:
        cost = sum(
            self.products.get(product, 0) * quantity
            for product, quantity in product_cart.items()
        )
        return cost

    def _build_receipt(self, customer: Customer, cost: float | int) -> str:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        purchases = [
            (f"{quantity} {product}{'s' if quantity > 1 else ''} for "
             f"{quantity * self.products[product]:g} dollars")
            for product, quantity in customer.product_cart.items()
        ]
        return (
            f"Date: {now}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought:\n"
            f"{'\n'.join(purchases)}\n"
            f"Total cost is {cost} dollars\n"
            f"See you again!\n"
        )

    def checkout(self, customer: Customer) -> str:
        cost = self.calculate_cart_cost(customer.product_cart)

        customer.pay(cost)

        return self._build_receipt(customer, cost)

    def __hash__(self) -> int:
        return hash(self.name)
