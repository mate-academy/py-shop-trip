from datetime import datetime
from unittest.mock import MagicMock
from app.customer import Customer
from app.trip import Trip


class Shop:
    def __init__(
        self,
        name: str,
        location: list,
        products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def total_products_cost(self, customer: Customer) -> dict:
        total_products_cost = {}
        for product, amount in self.products.items():
            if product in customer.product_cart:
                total_products_cost[product] = (
                    amount * customer.product_cart[product]
                )
        return total_products_cost

    @staticmethod
    def convert_to_int_if_possible(number: float) -> int:
        if number == int(number):
            return int(number)
        return number

    def shop_receipt(
        self,
        customer: Customer,
        cheapest_trip: Trip
    ) -> None:
        datetime_mock = MagicMock(datetime)
        datetime_mock.now.return_value = datetime(2021, 1, 4, 12, 33, 41)
        print(
            f'Date: {datetime_mock.now().strftime("%d/%m/%Y %H:%M:%S")}\n'
            f"Thanks, {customer.name}, for your purchase!\n"
            "You have bought:"
        )
        for product, cost in cheapest_trip.total_products_cost.items():
            print(f"{customer.product_cart[product]} {product}s for "
                  f"{self.convert_to_int_if_possible(cost)} dollars")
        print(
            f"Total cost is {cheapest_trip.total_product_price} dollars\n"
            f"See you again!\n"
        )
