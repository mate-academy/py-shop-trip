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

    def print_receipt(self, customer: Customer, date: datetime = None) -> None:
        if date is None:
            date = datetime.datetime.now()

        formatted_date = date.strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {formatted_date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for product, quantity in customer.product_cart.items():
            price_per_item = self.products[product]
            product_total = quantity * price_per_item
            if product_total.is_integer():
                product_total = int(product_total)
            total_cost += product_total
            product_for_receipt = str(product)
            if quantity > 1:
                product_for_receipt += "s"
            print(f"{quantity} {product_for_receipt} "
                  f"for {product_total} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
