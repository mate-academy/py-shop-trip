import datetime


class Shop:
    shops = {}

    def __init__(self,
                 name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products
        Shop.shops[name] = self

    def products_price(self, product_list: dict) -> float:
        total = 0
        for product, amount in product_list.items():
            total += self.products[product] * amount
        return total

    def buy_products(self, customer) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")

        for product, amount in customer.product_cart.items():
            print(f"{amount} {product}s for "
                  f"{self.products[product] * amount} dollars")

        print(f"Total cost is "
              f"{self.products_price(customer.product_cart)} dollars")
        print("See you again!\n")
