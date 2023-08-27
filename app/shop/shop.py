from dataclasses import dataclass

from app.customer.customer import Customer

from datetime import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def print_purchase_for_customer(self, customer: Customer) -> None:
        products_purchase = []
        for product, amount in customer.product_cart.items():
            product_cost = round(amount * self.products[product], 2)
            products_purchase.append(
                f"{amount} {product}s "
                f"for {product_cost} dollars"
            )
        products_purchase = "\n".join(products_purchase)

        total_cost = self.get_total_costs(customer)
        date = datetime(2021, 1, 4, 12, 33, 41)
        purchase = (
            "\n"
            f"Date: {date.strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!\n"
            f"You have bought: \n"
            f"{products_purchase}\n"
            f"Total cost is {total_cost} dollars\n"
            f"See you again!"
        )
        print(purchase)

    def get_total_costs(self, customer: Customer) -> float:
        costs = 0
        for product, amount in customer.product_cart.items():
            costs += round(self.products[product] * amount, 2)

        return costs

    def __hash__(self) -> int:
        return hash(self.name + str(self.location[0]) + str(self.location[1]))
