import datetime
from typing import Any


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def sum_of_products(self, product: dict) -> float:
        sum_of_products = (
            self.products["milk"] * product["milk"]
            + self.products["bread"] * product["bread"]
            + self.products["butter"] * product["butter"]
        )
        return sum_of_products

    def customers_trip(self,
                       customer: str,
                       func: Any,
                       function: Any) -> None:
        print(f"{customer}'s trip to the {self.name} costs {func + function}")

    def buy_products(self,
                     product: dict,
                     func: Any,
                     customer: str) -> None:
        dt = datetime.datetime.now()
        dt = dt.replace(year=2021,
                        month=1,
                        day=4,
                        hour=12,
                        minute=33,
                        second=41)
        dt = dt.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {dt}")
        print(f"Thanks, {customer}, for you purchase!")
        print("You have bought: ")
        print(f"{product['milk']} milks for "
              f"{self.products['milk'] * product['milk']} dollars")
        print(f"{product['bread']} breads for "
              f"{self.products['bread'] * product['bread']} dollars")
        print(f"{product['butter']} butters for "
              f"{self.products['butter'] * product['butter']} dollars")
        print(f"Total cost is {func} dollars")
        print("See you again!")
