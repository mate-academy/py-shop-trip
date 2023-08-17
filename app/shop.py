import datetime
import decimal


class Shop:
    shops = {}

    def __init__(self, name: str, location: list, products: dict):
        self.name = name
        self.location = location
        self.products = products
        Shop.shops[self.name] = self

    def products_price(self, products: dict):
        price = 0
        for product, amt in products.items():
            price += decimal.Decimal(self.products[product] * amt)
        return price

    def sell_products(self, products: dict, customer_name):
        dt = datetime.datetime.now()
        date_dt = dt.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date_dt}")
        print(f"Thanks, {customer_name}, for you purchase!")
        print("You have bought: ")
        total = 0
        for product, amt in products.items():
            price = (self.products[product] * amt)
            total += price
            print(f"{amt} {product}s for {price} dollars")
        print(f"Total cost is {total} dollars\nSee you again!\n")
