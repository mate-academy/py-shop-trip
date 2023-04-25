import dataclasses
from typing import Dict, List

from app.customer import Customer


@dataclasses.dataclass
class Shop:
    name: str
    location: List[int]
    products: Dict

    def print_receipt(self, customer: Customer):
        print(
            f"Date: 04/01/2021 12:33:41"
            f"Thanks, {customer.name}, for your purchase!"
            f"You have bought: "
            f"4 milks for 12 dollars"
            f"2 breads for 2 dollars"
            f"5 butters for 12.5 dollars"
            f"Total cost is 26.5 dollars"
            f"See you again!"
        )


shops = ...