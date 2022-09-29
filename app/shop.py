import datetime


class Shop:
    def __init__(self, shop: dict):
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def calculate_cost(self, product_cart: dict) -> int | None:
        total_cost = 0
        for product in product_cart:
            if product not in self.products:
                return False
            total_cost += product_cart[product] * self.products[product]
        return total_cost

    def print_purchase_receipt(self, name: str, product_cart: dict) -> None:
        print(datetime.datetime.now().strftime("Date: %d/%m/20%y %H:%M:%S"))
        print(f"Thanks, {name}, for you purchase!")
        print("You have bought: ")
        for product in product_cart:
            cost = product_cart[product] * self.products[product]
            print(f"{product_cart[product]} {item}s for {cost} dollars")
        print(f"Total cost is {self.calculate_cost(product_cart)} dollars")
        print("See you again!\n")
