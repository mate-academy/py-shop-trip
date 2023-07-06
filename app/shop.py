import dataclasses
import datetime

from typing import Union, Any


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict

    @staticmethod
    def customer_check(
            customer: Any,
            milks_coast: Union[int, float],
            breads_coast: Union[int, float],
            butters: Union[int, float],
            buy_coast: Union[int, float]
    ) -> None:
        dt = datetime.datetime.now()
        buy_date = dt.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {buy_date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        print(f"{customer.product_cart['milk']}"
              f" milks for {milks_coast} dollars")
        print(f"{customer.product_cart['bread']}"
              f" breads for {breads_coast} dollars")
        print(f"{customer.product_cart['butter']}"
              f" butters for {butters} dollars")
        print(f"Total cost is {buy_coast} dollars")
        print("See you again!\n")
