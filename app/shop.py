import datetime
from typing import List, Union, Dict


class Shop:
    def __init__(
            self,
            name: str,
            location: List[Union[int, float]],
            product: Dict[str, int]
    ) -> None:
        self.name = name
        self.location = location
        self.product = product

    @staticmethod
    def format_cost(cost: float) -> Union[int, float]:
        if cost == int(cost):
            return int(cost)
        return round(cost, 2)

    def print_receipt(
            self,
            customer_name: str,
            product_cart: Dict[str, int],
            total_cost: float
    ) -> None:
        curr_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {curr_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in product_cart.items():
            price = self.product[product]
            total_item = price * quantity

            print(f"{quantity} {product}s "
                  f"for {self.format_cost(total_item)} dollars")

        print(f"Total cost is {self.format_cost(total_cost)} dollars")
        print("See you again!\n")
