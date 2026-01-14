import datetime
from typing import Dict
from app.customer import Customer


class Shop:
    def __init__(
            self, name: str, location: list, products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def trip_cost(self, customer: Customer, fuel_price: float) -> float:
        distance = customer.distance_to(self.location)
        fuel_cost = 2 * customer.car.fuel_needed(distance) * fuel_price
        products_cost = customer.products_total(self.products)
        return fuel_cost + products_cost

    def _format_price(self, price: float) -> float:
        return int(price) if float(price).is_integer() else round(price, 2)

    def print_receipt(self, customer: Customer) -> None:
        now = datetime.datetime.now()
        print()
        print(f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total = 0.0
        for product, qty in customer.product_cart.items():
            price = self.products[product] * qty
            total += price
            print(f"{qty} {product}s for {self._format_price(price)} dollars")

        print(f"Total cost is {self._format_price(total)} dollars")
        print("See you again!")
        print()
