import datetime


class Shop:
    def __init__(self, shops: dict) -> None:
        self.name = shops["name"]
        self.location = shops["location"]
        self.products = shops["products"]

    def calculate_price(self, product_cart: dict) -> float:
        total_price = 0
        for product in product_cart:
            total_price += product_cart[product] * self.products[product]
        return total_price

    def print_receipt(self, other: str) -> None:
        print(datetime.datetime.now().strftime("Date: %d/%m/20%y %H:%M:%S"))

        print(f"Thanks, {other.name}, for you purchase!")

        print("You have bought: ")
        for product in other.product_cart:
            price = other.product_cart[product] * self.products[product]
            print(f"{other.product_cart[product]} "
                  f"{product}s for {price} dollars")

        print(f"Total cost is "
              f"{self.calculate_price(other.product_cart)} dollars")

        print("See you again!\n")
