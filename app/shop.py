import math
import datetime

from app.customer import Customer


class Shop:

    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_distance(self, customer: Customer) -> float:
        return math.sqrt(
            (self.location[0] - customer.location[0]) ** 2
            + (self.location[1] - customer.location[1]) ** 2)

    def calculate_trip_cost(
            self,
            customer: Customer,
            fuel_price: float
    ) -> float:
        distance_to_shop = self.calculate_distance(customer)
        fuel_cost_to_shop = ((distance_to_shop / 100)
                             * customer.car.fuel_consumption * fuel_price)
        total_product_cost = sum(self.products[item] * count
                                 for item, count
                                 in customer.product_cart.items())

        total_cost = fuel_cost_to_shop * 2 + total_product_cost

        return round(total_cost, 2)

    def make_purchase(self, customer: Customer) -> float:
        total_products_cost = 0
        receipt = []

        for product, count in customer.product_cart.items():
            if product in self.products:
                total_products_cost += count * self.products[product]
                receipt.append(f"{count} {product}s for "
                               f"{self.products[product] * count:g} dollars")

        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {current_time}\n"
              f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for item in receipt:
            print(item)
        print(f"Total cost is {total_products_cost} dollars")
        print("See you again!\n")

        return total_products_cost
