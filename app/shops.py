import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def purchase_receipt(self,
                         customer_name: str,
                         customer_products: dict) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {date}\n"
              f"Thanks, {customer_name}, for your purchase!\n"
              f"You have bought: ")
        self.products_receipt(customer_products)

        print(f"Total cost is {self.buy_products(customer_products)} dollars\n"
              f"See you again!\n")

    def buy_products(self, customer_products: dict) -> int | float:
        return sum(customer_products[product]
                   * self.products[product]
                   for product in self.products)

    def products_receipt(self, customer_products: dict) -> None:
        for product, count in customer_products.items():
            end_with_s = "s" if count != 1 else ""
            print(f"{count} {product}{end_with_s} for "
                  f"{count * self.products[product]} dollars")
