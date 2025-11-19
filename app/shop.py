import datetime
from app.utils import format_number


class Shop:
    def __init__(
        self,
        name: str,
        location: list[int],
        products: dict[str, int]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def purchase_cost(self, product_cart: dict[str, int]) -> float:
        total_cost = 0.0
        for product, quantity in product_cart.items():
            if product in self.products:
                total_cost += self.products[product] * quantity
            else:
                raise ValueError(f"Product {product} is not available "
                                 f"in shop {self.name}")

        return total_cost

    def proceed_purchase(
        self, customer_name: str,
        product_cart: dict[str, int]
    ) -> None:
        datestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {datestamp}")

        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, quantity in product_cart.items():
            if product in self.products:
                price = self.products[product] * quantity
                total_cost += price
                if isinstance(price, int) or price.is_integer():
                    price = int(price)
                print(f"{quantity} {product}s for {price} dollars")

        print(f"Total cost is {format_number(total_cost)} dollars")
        print("See you again!")
