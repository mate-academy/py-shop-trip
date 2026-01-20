import datetime


class Shop:
    def __init__(self, shop):
        self.name = shop["name"]
        self.products = shop["products"]
        self.location = shop["location"]

    def cost(self, product_cart):
        if set(product_cart) <= set(self.products):
            cost = 0
            for product in product_cart:
                cost += product_cart[product] * self.products[product]
        else:
            return None
        return cost

    def print_cash_receipt(self, name, product_cart):
        print("Date:", datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {name}, for you purchase!")
        print("You have bought: ")
        for product in product_cart:
            for product_ in self.products:
                if product == product_:
                    cost = product_cart[product] * self.products[product_]
                    print(
                        f"{product_cart[product]} {product}s for "
                        f"{cost} dollars")
        print(f"Total cost is {self.cost(product_cart)} dollars")
        print("See you again!\n")
