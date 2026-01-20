import datetime


class Shop:
    def __init__(self, shops: dict) -> None:
        self.name = shops["name"]
        self.location = shops["location"]
        self.products = shops["products"]

    def total_product_cost(self, product_cart: dict) -> int | float:
        purchase_amount = 0
        for product in product_cart:
            purchase_amount += product_cart[product] * self.products[product]
        return purchase_amount

    def print_receipt(self, name: str, product_cart: dict) -> None:
        print(datetime.datetime.now().strftime("Date: %d/%m/20%y %H:%M:%S"))
        print(f"Thanks, {name}, for you purchase!")
        print("You have bought: ")
        for product in product_cart:
            cost = product_cart[product] * self.products[product]
            print(f"{product_cart[product]} {product}s for {cost} dollars")
        print(f"Total cost is {self.total_product_cost(product_cart)} dollars")
        print("See you again!\n")
