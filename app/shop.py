import datetime


class Shop:
    def __init__(self, dct: dict) -> None:
        self.name = dct["name"]
        self.location = dct["location"]
        self.products: dict = dct["products"]

    def purchases(self, product_cart: dict) -> float:
        purchases = 0
        for name, count in product_cart.items():
            if name in self.products:
                purchases += count * self.products[name]

        return purchases

    def checkout(self, name: str, groceries: dict) -> None:
        time = datetime.datetime.now()
        formatted_time = time.strftime("%d/%m/%Y %H:%M:%S")
        print("")
        print(f"Date: {formatted_time}")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")
        for grocery, count in groceries.items():
            amount = count * self.products[grocery]
            print(f"{count} {grocery}s for {amount:g} dollars")

        print(f"Total cost is {self.purchases(groceries):g} dollars")
        print("See you again!")
        print("")
