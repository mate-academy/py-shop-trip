import datetime

from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: list) -> None:
        self. name = name
        self.location = location
        self.products = products

    def print_list(self, customer: Customer) -> str:
        cart = ""
        total = 0
        for customer_product in customer.product_cart:
            for product in self.products:
                if customer_product.product_name == product.name:
                    products_cost = (customer_product.product_amount
                                     * product.price)
                    cart += (f"{customer_product.product_amount}"
                             f" {product.name}s"
                             f" for {products_cost} dollars\n")
                    total += (customer_product.product_amount
                              * product.price)

        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        return (f"Date: {date}\n"
                f"Thanks, {customer.name}, for you purchase!\n"
                f"You have bought: \n"
                f"{cart}"
                f"Total cost is {total} dollars\n"
                f"See you again!"), total
