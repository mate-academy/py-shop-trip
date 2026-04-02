import datetime
from decimal import Decimal, ROUND_HALF_UP


def format_money(amount: float | Decimal) -> str:
    dem: Decimal = Decimal(str(amount)).quantize(Decimal("0.01"),
                                                 rounding=ROUND_HALF_UP)
    return str(dem.normalize())


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def total_cost(self, product_cart: dict) -> Decimal:
        cost = Decimal("0.00")
        for product, qty in product_cart.items():
            if product in self.products:
                cost += Decimal(str(self.products[product])) * qty
        return cost

    def receipt(self, customer_name: str, product_cart: dict) -> None:
        print(f"\nDate: {datetime.datetime.now().strftime('%d/%m/%Y '
                                                          '%H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total = Decimal("0.00")

        for product, qty in product_cart.items():
            price = (Decimal(str(self.products[product])) * qty).quantize(
                Decimal("0.01"), ROUND_HALF_UP
            )
            total += price
            plural = f"{product}s" if qty > 1 else product
            print(f"{qty} {plural} for {format_money(price)} dollars")

        print(f"Total cost is {format_money(total)} dollars")
        print("See you again!\n")
