import datetime

from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def give_receipt(
            self,
            customer: Customer,
            total_cost: float
    ) -> None:
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_date}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought:")

        for product, amount in customer.product_cart.items():
            product_cost = amount * self.products[product]
            if product_cost == int(product_cost):
                cost_str = str(int(product_cost))
            else:
                cost_str = str(product_cost)

            print(f"{amount} {product}s for {cost_str} dollars")
        print(f"Total cost is {total_cost} dollars\nSee you again!\n")
