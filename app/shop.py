import datetime


class Shop:
    def __init__(self, shops: dict) -> None:
        self.name = shops["name"]
        self.location = shops["location"]
        self.products = shops["products"]

    def calculate_costs(self, cart: dict) -> float:
        total_price = 0
        for product in cart:
            total_price += cart[product] * self.products[product]
        return total_price

    def receipt(self, name: str, cart: dict) -> None:
        print(datetime.datetime.now().strftime("Date: %d/%m/20%y %H:%M:%S"))
        print(f"Thanks, {name}, for you purchase!")
        print("You have bought: ")
        for product in cart:
            cost = cart[product] * self.products[product]
            print(
                f"{cart[product]} "
                f"{product}s for {cost} dollars"
            )
        print(f"Total cost is {self.calculate_costs(cart)} dollars")
        print("See you again!\n")
