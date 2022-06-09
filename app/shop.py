import datetime


class Shop:
    def __init__(self, shop_info: dict):
        self.name = shop_info["name"]
        self.location = shop_info["location"]
        self.products = shop_info["products"]

    def sell_products(self, customer):
        bill_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        products = customer.product_cart
        bill = 0

        print(f"Date: {bill_time}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        for product, amount in products.items():
            products_cost = self.products[product] * amount
            bill += products_cost
            print(f"{amount} {product}s for {products_cost} dollars")
        print(f"Total cost is {bill} dollars")
        print("See you again!\n")
