import datetime
from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list[int],
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_check(self, customer: Customer) -> None:

        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for product in customer.products_cart:

            amount = customer.products_cart[product]
            price_for_amount = (self.products[product]
                                * customer.products_cart[product])
            price_for_amount = int(price_for_amount) \
                if price_for_amount == int(price_for_amount) \
                else price_for_amount

            print(f"{amount} {product}s "
                  f"for {price_for_amount} dollars")
            total_cost += (self.products[product]
                           * customer.products_cart[product])
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
