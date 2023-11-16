import datetime
from typing import Dict
from dataclasses import dataclass
from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list[int]
    products: Dict[str, float | int]

    def calculate_trip_cost(
            self,
            customer: Customer,
            fuel_price: float
    ) -> float:
        distance_to_shop = customer.calculate_distance(self.location)
        trip_cost = customer.car.calculate_fuel_cost(
            distance_to_shop,
            fuel_price
        )
        product_cost = self.calculate_product_cost(customer)
        return trip_cost + product_cost

    def make_purchase(self, customer: Customer) -> None:
        total_cost = self.calculate_product_cost(customer)
        if total_cost <= customer.money:
            customer.money -= total_cost
            self.print_receipt(customer)
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase at {self.name}")

    def calculate_product_cost(
            self,
            customer: Customer
    ) -> float:
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            if product in self.products:
                total_cost += self.products[product] * quantity
        return total_cost

    def print_receipt(
            self,
            customer: Customer
    ) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        total_cost = self.calculate_product_cost(customer)
        print(f"\nDate: {now}\nThanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in customer.product_cart.items():
            cost = self.products[product] * quantity
            if cost == int(cost):
                cost = int(cost)
            print(f"{quantity} {product}s for {cost} dollars")
        print(f"Total cost is {total_cost} dollars\nSee you again!\n")
