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

    def get_check(self, customer: Customer) -> None:
        data = datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S")

        print(f"Date: {data}")
        print(f"Thanks, {customer}, for your purchase!")
        print("You have bought: ")

        for product, amount in customer.product_cart.items():
            price = amount * self.products[product]
            print(f"{amount} {product}s for {price} dollars")
            for product_name, total_amount in customer.total_shopping_list_price(self):
                print(f"Total cost is {total_amount} dollars")
            print("See you again!")
