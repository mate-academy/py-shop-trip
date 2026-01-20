import datetime


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict):
        self.name = name
        self.products = products
        self.location = location

    def calculate_prices(self, name_product: str, count_product: int):
        return self.products[name_product] * count_product

    def purchase(self, customer_name: str, customer_products: dict):
        now = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for you purchase!")
        print("You have bought: ")
        total = 0
        for product in customer_products:
            price_products = self.calculate_prices(product[0], product[1])
            total += price_products
            print(f"{product[1]} {product[0]}s for {price_products} dollars")
        print(f"Total cost is {total} dollars")
        print("See you again!\n")
