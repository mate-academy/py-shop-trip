import datetime
from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def products_price(self, customer: Customer) -> float | int | str:
        price = 0

        for name, value in customer.product_cart.items():
            if name not in self.products:
                price = -1
                return f"There is not {name} in {self.name}"

            price += self.products[name] * value

        return price

    def print_purchase_receipt(self, customer: Customer) -> None:
        today = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        total_price = 0

        print(
            f"Date: {today}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            "You have bought: "
        )
        for product, value in customer.product_cart.items():
            product_price = value * self.products[product]
            print(f"{value} {product}s for {product_price} dollars")
            total_price += product_price

        print(
            f"Total cost is {total_price} dollars\n"
            f"See you again!\n"
        )
