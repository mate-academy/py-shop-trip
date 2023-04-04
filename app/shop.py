import datetime


class Shop:
    def __init__(
        self, name: str, products: dict[str, float], location: list[int]
    ) -> None:
        self.name = name
        self.products = products
        self.location = location if location else [0, 0]

    def __repr__(self) -> str:
        return f"{self.name}, {self.location}, {self.products}"

    def print_check(self, customer: dict) -> str:
        total_cost = 0
        current_time = datetime.datetime.now()
        text_check = (
            f"Date: {current_time.strftime('%d/%m/%Y %H:%M:%S')}"
            + f"\nThanks, {customer.name}, for you purchase!\n"
            + "You have bought: \n"
        )
        for product, item in customer.product_cart.items():
            product_cost = round(item * self.products[product], 2)
            total_cost += product_cost
            text_check += f"{item} {product}s for {product_cost} dollars\n"
        text_check += \
            f"Total cost is {total_cost} dollars\n" "See you again!\n"
        return text_check
