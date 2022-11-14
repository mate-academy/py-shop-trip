import datetime


class Shop:
    def __init__(self, datasource: dict) -> None:
        self.name = datasource["name"]
        self.location = datasource["location"]
        self.products = datasource["products"]

    def print_purchase(self, customer_name: str, products: dict) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for you purchase!")
        print("You have bought: ")
        total = 0
        for product_name, number in products.items():
            print(f"{number} {product_name}s for "
                  f"{number * self.products[product_name]} dollars")
            total += number * self.products[product_name]
        print(f"Total cost is {total} dollars")
        print("See you again!\n")
