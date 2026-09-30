import dataclasses
import math
import datetime

from app.customer import Customer


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict

    @staticmethod
    def _format_number(value: float) -> str:
        rounded = round(value, 2)
        if rounded == int(rounded):
            return str(int(rounded))
        return str(rounded)

    def distanse_to(self, customer: Customer) -> float:
        return math.dist(self.location, customer.location)

    def fuel_cost_one_way(self, customer: Customer,
                          fuel_price: float) -> float:
        distanse = self.distanse_to(customer)
        liters = distanse * customer.car.fuel_consumption / 100
        return liters * fuel_price

    def product_cost(self, customer: Customer) -> float:
        return sum(
            self.products[product] * amount
            for product, amount in customer.product_cart.items()
        )

    def trip_cost(self, customer: Customer, fuel_price: float) -> float:
        fuel_cost = self.fuel_cost_one_way(customer, fuel_price)
        return self.product_cost(customer) + 2 * fuel_cost

    def sell(self, customer: Customer) -> None:
        customer.location = list(self.location)

        total_cost = 0
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for product, amount in customer.product_cart.items():
            price = self.products[product] * amount
            total_cost += price
            print(f"{amount} {product}s for "
                  f"{self._format_number(price)} dollars")

        print(f"Total cost is {self._format_number(total_cost)} dollars")
        print("See you again!")
        print()
