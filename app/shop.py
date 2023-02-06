import datetime
from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_shopping_cost(self, customer: Customer) -> int | float:
        shopping_cost = 0
        for product in customer.product_cart:
            if product in self.products:
                product_quantity = customer.product_cart[product]
                product_price = self.products[product]
                total_product_cost = product_quantity * product_price
                shopping_cost += total_product_cost
        return shopping_cost

    def get_best_option(self, customer: Customer) -> None:
        print(f"{customer.name} rides to {self.name}")

    def get_receipt(self, customer: Customer) -> None:
        current_date = datetime.datetime.now()
        print(f"\nDate: {current_date.strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {customer.name}, for you purchase!\n"
              f"You have bought: ")

        for product in customer.product_cart:
            number = customer.product_cart[product]
            price = number * self.products[product]
            print(f"{number} {product}s for {price} dollars")
        print(f"Total cost is {self.get_shopping_cost(customer)} dollars\n"
              f"See you again!\n")
