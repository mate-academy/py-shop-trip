import datetime


class Shop:
    def __init__(self, shop: dict):
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]

    def calculate_cost(self, product_cart: dict) -> int | None:
        if set(self.products) >= set(product_cart):
            total_cost = 0
            for item in product_cart:
                if item not in self.products:
                    return False
                total_cost += product_cart[item] * self.products[item]
        else:
            return None

        return total_cost

    def print_purchase_receipt(self, name: str, product_cart: dict) -> None:
        print(datetime.datetime.now().strftime("Date: %d/%m/20%y %H:%M:%S"))
        print(f"Thanks, {name}, for you purchase!")
        print("You have bought: ")
        for item in product_cart:
            cost = product_cart[item] * self.products[item]
            print(f"{product_cart[item]} {item}s for {cost} dollars")
        print(f"Total cost is {self.calculate_cost(product_cart)} dollars")
        print("See you again!\n")
