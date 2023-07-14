import math
from typing import Union


class CostCalculation:
    def __init__(self, customers, shops, fuel_price):
        self.customers = customers
        self.shops = shops
        self.fuel_price = fuel_price

        self.results = {}

    def calculation(self) -> Union[int, float]:

        for customer in self.customers.values():
            self.results[customer] = []

            for shop in self.shops.values():
                trip_total_cost = 0
                trip_total_cost += (
                        (self.fuel_price * customer.car["fuel_consumption"])
                        / 100 * math.dist(customer.location, shop.location)
                        * 2
                )

                for product in customer.product_cart.items():
                    if product[0] in shop.products:
                        trip_total_cost += (
                                shop.products[product[0]] * product[1]
                        )

                self.results[customer].append({shop: trip_total_cost})

        return self.results


if __name__ == '__main__':
    pass
