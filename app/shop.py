import datetime
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict


def format_money(amount: float) -> str:
    dem: Decimal = Decimal(str(amount)).quantize(Decimal("0.01"),
                                                 rounding=ROUND_HALF_UP)
    return str(dem.normalize())


class Shop:
    def __init__(self,
                 name: str,
                 location: list[float],
                 products: Dict[str, float]) -> None:
        self.name: str = name
        self.location: list[float] = location
        self.products: Dict[str, float] = products

    def total_cost(self, product_cart: Dict[str, int]) -> Decimal:
        cost: Decimal = Decimal("0.00")
        for product, qty in product_cart.items():
            if product in self.products:
                cost += Decimal(str(self.products[product])) * qty
        return cost.quantize(Decimal("0.01"), ROUND_HALF_UP)

    def receipt(self,
                customer_name: str,
                product_cart: Dict[str, int]) -> None:
        print(f"\nDate: {datetime.datetime.now().strftime('%d/%m/%Y '
                                                          '%H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total: Decimal = Decimal("0.00")

        for product, qty in product_cart.items():
            # Only process items that exist in this shop
            if product not in self.products:
                continue

            price: Decimal = (Decimal(str(
                self.products[product])) * qty).quantize(
                Decimal("0.01"), ROUND_HALF_UP
            )
            total += price

            plural: str = f"{product}s" if qty > 1 else product
            print(f"{qty} {plural} for {format_money(float(price))} dollars")

        print(f"Total cost is {format_money(float(total))} dollars")
        print("See you again!\n")
