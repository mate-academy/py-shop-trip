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
        print(f"Thanks, {customer_name}, for you purchase!\nYou have bought:")
        price = 0
        for product, amt in products.items():
            print(f"{amt} {product}s for {self.products[product]} dollars")
            price += decimal.Decimal(self.products[product] * amt)
        print(f"Total cost is {price} dollars\nSee you again!")
