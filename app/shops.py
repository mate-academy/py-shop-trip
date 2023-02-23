import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def purchase_receipt(self,
                         customer_name: str,
                         customer_products: dict) -> None:
        date = datetime.datetime.now()
        print(f"Date: {date.strftime('%d')}/"
              f"{date.strftime('%m')}/"
              f"{date.strftime('%Y')}"
              f" {date.strftime('%H')}:"
              f"{date.strftime('%M')}:"
              f"{date.strftime('%S')}\n"
              f"Thanks, {customer_name}, for you purchase!\n"
              f"You have bought: \n"
              f"{customer_products['milk']} milks for "
              f"{customer_products['milk'] * self.products['milk']} dollars\n"
              f"{customer_products['bread']} breads for "
              f"{customer_products['bread'] * self.products['bread']} "
              f"dollars\n"
              f"{customer_products['butter']} butters for "
              f"{customer_products['butter'] * self.products['butter']} "
              f"dollars\n"
              f"Total cost is {self.buy_products(customer_products)} dollars\n"
              f"See you again!")

    def buy_products(self, customer_products: dict) -> int | float:
        return sum(customer_products[product]
                   * self.products[product]
                   for product in self.products)
