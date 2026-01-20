import datetime


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_price_of_products(self, customer_products: dict) -> float:
        return sum(self.products[product] * count
                   for product, count in customer_products.items())

    def bought(self, name: str, customer_products: dict) -> None:
        print("")
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")

        for product, count in customer_products.items():
            _summa = self.products[product] * count
            if int(_summa) == _summa:
                _summa = int(_summa)
            print(f"{count} {product}s for {round(_summa, 2)} dollars")

        print(f"Total cost is "
              f"{self.get_price_of_products(customer_products)} "
              f"dollars")
        print("See you again!\n")
