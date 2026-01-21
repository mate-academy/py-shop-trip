from math import sqrt

from app.customer import Customer


class Shop:
    def __init__(
        self,
        name: str,
        location: list,
        prices: dict,
    ) -> None:
        self.name = name
        self.location = location
        self.prices = prices

    def calculate_shopping_cost(
            self,
            customer: Customer
    ) -> float:
        result = 0
        for pd in customer.products.keys():
            result += self.prices[pd] * customer.products[pd]
        return result

    def cost_to_drive(
            self,
            customer: Customer
    ) -> float:
        return (sqrt((customer.location[0]
                      - self.location[0]) ** 2
                     + (customer.location[1] - self.location[1]) ** 2)
                * (customer.car.fuel_consumption / 100))
