import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def make_purchase(self, customer: object) -> None:
        customer.location = self.location
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for you purchase!\n"
              f"You have bought: ")

        for product, quantity in customer.product_cart.items():
            print(f"{quantity} {product}s for "
                  f"{quantity * self.products.get(product)} dollars")

        print(f"Total cost is "
              f"{customer.calculate_products_cost(self)} dollars\n"
              f"See you again!\n")
