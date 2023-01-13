import datetime
from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def shop_expenses(self, customer: Customer) -> float | int:
        price = 0

        for product in self.products:
            if product in customer.product_cart:
                price += (
                    customer.product_cart[product]
                    * self.products[product]
                )

        return price

    def shopping(self, customer: Customer) -> None:
        current_datetime = datetime.datetime.now()
        print(f"{customer.name} rides to {self.name}\n"
              f"\nDate: {current_datetime.strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {customer.name}, for you purchase!\n"
              f"You have bought: ")

        for product in customer.product_cart:
            print(f"{customer.product_cart[product]} {product}s for "
                  f"{customer.product_cart[product] * self.products[product]} "
                  f"dollars")
        print(f"Total cost is {self.shop_expenses(customer)} dollars\n"
              f"See you again!\n")
