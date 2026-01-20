import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict[str, int | float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def make_purchases(self, customer: object) -> None:
        print(f"Date: {self._get_current_datetime()}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_sum = 0
        for product, amount in customer.product_cart.items():
            price = amount * self.products.get(product)
            price = int(price) if price == int(price) else price
            print(f"{amount} {product}s for {price} dollars")
            total_sum += price

        customer.money -= total_sum
        print(f"Total cost is {total_sum} dollars")
        print("See you again!\n")

    @staticmethod
    def _get_current_datetime() -> str:
        current_datetime = datetime.datetime.now()
        str_current_datetime = current_datetime.strftime("%d/%m/%Y %H:%M:%S")
        return str_current_datetime

    def __repr__(self) -> str:
        return self.name
