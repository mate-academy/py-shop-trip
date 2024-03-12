import datetime
from typing import Tuple, Dict, Any


class Shop:
    def __init__(
            self,
            name: str,
            location: Tuple[float, float],
            products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def generate_receipt(
            self,
            customer: Any,
            datetime_now: datetime.datetime,
            total_cost: float
    ) -> None:
        from .customer import Customer
        assert (
            isinstance(customer, Customer)
        ), "customer must be an instance of Customer"
        print(f"\nDate: {datetime_now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in customer.product_cart.items():
            product_price = self.products[product] * quantity
            product_price_float = float(product_price)
            price_str = ((f""
                         f"{int(product_price_float)}")
                         if product_price_float.is_integer()
                         else f"{product_price_float:.1f}"
                         )
            print(f"{quantity} {product}s for {price_str} dollars")
        total_cost_float = float(total_cost)
        total_cost_str = (f"{total_cost:.1f}"
                          if not total_cost.is_integer()
                          else f"{int(total_cost_float):}"
                          )
        print(f"Total cost is {total_cost_str} dollars")
        print("See you again!\n")
