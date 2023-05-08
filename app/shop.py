from datetime import datetime


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def count_product(self, cust_cart: dict) -> list:
        total = [val * self.products[key] for key, val in cust_cart.items()]
        return total

    def bill(self, customer_name: str, customer_prod: dict) -> None:
        total_price = []
        date = datetime(2021, 1, 4, 12, 33, 41).strftime("%d/%m/%Y %H:%M:%S")
        print(f"{customer_name} rides to {self.name}\n")
        print(f"Date: {date}\n"
              f"Thanks, {customer_name}, for your purchase!")
        print("You have bought: ")
        for key, value in customer_prod.items():
            price = value * self.products[key]
            print(f"{value} {key}s for {price} dollars")
            total_price.append(price)
        print(f"Total cost is {sum(total_price)} dollars\nSee you again!\n")
