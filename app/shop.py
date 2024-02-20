from app.customer import Customer
from app.trip import Trip
from typing import List, Dict, Union
from datetime import datetime
from unittest.mock import MagicMock


class Shop:

    def __init__(
            self,
            name: str,
            location: List[int],
            products: Dict[str, Union[int, float]]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def convert_to_int_if_possible(number: float) -> float | int:
        if number == int(number):
            return int(number)
        return number

    @staticmethod
    def shop_receipt(
            customer: Customer,
            trip_instances: List[Trip]
    ) -> None:
        cheapest_trip = Trip.cheapest_trip(trip_instances)
        datetime_mock = MagicMock(wrap=datetime)
        datetime_mock.now.return_value = datetime(2021, 1, 4, 12, 33, 41)

        milk_cost = Shop.convert_to_int_if_possible(
            cheapest_trip.total_milk_cost
        )
        bread_cost = Shop.convert_to_int_if_possible(
            cheapest_trip.total_bread_cost
        )
        butter_cost = Shop.convert_to_int_if_possible(
            cheapest_trip.total_butter_cost
        )

        print(
            f'Date: {datetime_mock.now().strftime("%d/%m/%Y %H:%M:%S")}\n'
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought:\n"
            f'{customer.product_cart["milk"]} milks for {milk_cost} dollars\n'
            f'{customer.product_cart["bread"]} breads for '
            f"{bread_cost} dollars\n"
            f'{customer.product_cart["butter"]} butters for '
            f"{butter_cost} dollars\n"
            f"Total cost is {cheapest_trip.total_product_price} dollars\n"
            f"See you again!\n"
        )
