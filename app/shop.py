import datetime


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calc_product_cost(self, product_cart: dict) -> int | None:
        total = 0
        for product in product_cart:
            total += product_cart[product] * self.products[product]
        return total

    def print_check(self, name: str, product_cart: dict) -> None:
        print(datetime.datetime.now().strftime("Date: %d/%m/20%y %H:%M:%S"))
        print(f"Thanks, {name}, for you purchase!")
        print("You have bought: ")
        for product in product_cart:
            cost = product_cart[product] * self.products[product]
            print(f"{product_cart[product]} {product}s for {cost} dollars")
        print(f"Total cost is {self.calc_product_cost(product_cart)} dollars")
        print("See you again!\n")
