from datetime import datetime

from app.customer import Customer


class Shop:
    def __init__(self,
                 name: str,
                 location: list[int],
                 products: dict[str:int]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __repr__(self) -> str:
        return f"{self.name}"

    def receipt(self, customer: Customer) -> float:
        for product in customer.product_cart.keys():
            if product not in self.products:
                raise RuntimeError(f"Product {product} "
                                   f"is not sell in this store({self.name})")

        total_sum = 0.0
        now = datetime.now()
        print(now.strftime("Date: " + "%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product in customer.product_cart.keys():
            _sum = customer.product_cart[product] * self.products[product]
            if _sum.is_integer():
                _sum = int(_sum)
            print(f"{customer.product_cart[product]} "
                  f"{product}s for {_sum} dollars")
            total_sum += _sum

        print(f"Total cost is {total_sum} dollars")
        print("See you again!\n")

        return total_sum
