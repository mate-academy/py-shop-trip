from datetime import datetime


class Shop:

    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer: object) -> None:
        milk_quantity = customer.product_cart["milk"]
        bread_quantity = customer.product_cart["bread"]
        butter_quantity = customer.product_cart["butter"]
        milk_price = self.products["milk"]
        bread_price = self.products["bread"]
        butter_price = self.products["butter"]
        total_milk = milk_quantity * milk_price
        total_bread = bread_quantity * bread_price
        total_butter = butter_quantity * butter_price
        total = total_milk + total_bread + total_butter
        date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought:")
        print(f"{milk_quantity} milks for {total_milk} dollars")
        print(f"{bread_quantity} breads for {total_bread} dollars")
        print(f"{butter_quantity} butters for {total_butter} dollars")
        print(f"Total cost is {total} dollars")
        print("See you again!\n")

    def total_groceries_cost(self, customer: object) -> int:
        milk_quantity = customer.product_cart["milk"]
        bread_quantity = customer.product_cart["bread"]
        butter_quantity = customer.product_cart["butter"]
        milk_price = self.products["milk"]
        bread_price = self.products["bread"]
        butter_price = self.products["butter"]
        total_milk = milk_quantity * milk_price
        total_bread = bread_quantity * bread_price
        total_butter = butter_quantity * butter_price
        total = total_milk + total_bread + total_butter
        return total
