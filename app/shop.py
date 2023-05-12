import datetime
import json


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def count_product(self, cust_cart: dict) -> list[int]:
        return [amount * self.products[product]
                for product, amount in cust_cart.items()]

    def bill(self, customer_name: str, customer_cart: dict) -> None:
        total_price = []
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{customer_name} rides to {self.name}\n")
        print(f"Date: {date}\n"
              f"Thanks, {customer_name}, for your purchase!")
        print("You have bought: ")
        for product, amount in customer_cart.items():
            price = amount * self.products[product]
            print(f"{amount} {product}s for {price} dollars")
            total_price.append(price)
        print(f"Total cost is {sum(total_price)} dollars\nSee you again!\n")


with open("app/config.json") as config:
    infos = json.load(config)

shops_dict = {
    shop["name"]: Shop(
        shop["name"],
        shop["location"],
        shop["products"]
    )
    for shop in infos["shops"]
}
