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
        dt = dt.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {dt}\n"
              f"Thanks, {customer}, for you purchase!\n"
              "You have bought: \n"
              f"{product['milk']} milks for "
              f"{self.products['milk'] * product['milk']} dollars\n"
              f"{product['bread']} breads for "
              f"{self.products['bread'] * product['bread']} dollars\n"
              f"{product['butter']} butters for "
              f"{self.products['butter'] * product['butter']} dollars\n"
              f"Total cost is {func} dollars\n"
              "See you again!")
