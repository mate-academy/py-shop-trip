import datetime
from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_product_cost(self, product: str, number: int) -> int | float:
        result = self.products[product] * number
        return int(result) if result % 1 == 0 else result

    def calculate_products_total_cost(self, products: dict) -> int | float:
        return sum(
            self.calculate_product_cost(product, number)
            for product, number in products.items()
        )

    def create_receipt(
            self,
            customer_name: str,
            customer_products: dict
    ) -> None:
        timestamp = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {timestamp}\n"
              f"Thanks, {customer_name}, for your purchase!\n"
              f"You have bought:")

        for product, number in customer_products.items():
            product_cost = round(
                self.calculate_product_cost(product, number),
                2
            )
            if number > 1:
                product += "s"
            print(f"{number} {product} for {product_cost} dollars")

        products_total_cost = round(
            self.calculate_products_total_cost(customer_products),
            2
        )
        print(f"Total cost is {products_total_cost} dollars\n"
              f"See you again!\n")
