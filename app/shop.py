import datetime
from typing import List, Dict, Any


class Shop:

    def __init__(
            self, name: str,
            location: List[float],
            products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def _fmt(self, number: Any) -> str:

        value = round(float(number), 2)
        if value.is_integer():
            return str(int(value))
        else:
            return f"{value:.2f}".rstrip("0").rstrip(".")

    def calculate_products_cost(
            self,
            product_cart: Dict[str, int]
    ) -> float:
        total_product_cost = 0.0

        for product_name, quantity in product_cart.items():

            if product_name in self.products:
                price = self.products[product_name]
                total_product_cost += price * quantity
            else:
                raise ValueError(
                    f"Product {product_name} not available in {self.name}"
                )
        return total_product_cost

    def print_receipt(
            self,
            customer_name: str,
            product_cart: Dict[str, int]
    ) -> None:
        data_now = datetime.datetime.now()
        date_time = data_now.strftime("%d/%m/%Y %H:%M:%S")
        print("\n" f"Date: {date_time}\n" f"Thanks, {customer_name}, "
              f"for your purchase!\n" "You have bought:")

        for product_name, quantity in product_cart.items():

            if product_name in self.products:
                price = self.products[product_name]
                cost_of_item = price * quantity
                suffix = "s" if quantity > 1 else ""

                print(
                    f"{quantity} {product_name}"
                    f"{suffix} for {self._fmt(cost_of_item)} dollars"
                )
        total = self.calculate_products_cost(product_cart)
        print(f"Total cost is {self._fmt(total)} "
              f"dollars\n" "See you again!\n" "")
