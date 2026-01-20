import datetime


class Shop:
    def __init__(self, shops: dict) -> None:
        self.name = shops["name"]
        self.location = shops["location"]
        self.products = shops["products"]

    def calculate_products_price(self, product_cart: dict) -> float:
        price = 0

        for key, value in product_cart.items():
            price += value * self.products[key]

        return price

    def receipt(self, name: str, product_cart: dict) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {name}, for you purchase!")
        print("You have bought: ")

        total_cost = 0
        for product in self.products:
            price = self.products[product] * product_cart[product]
            total_cost += price
            print(f"{product_cart[product]} {product}s for {price} dollars")

        print(f"Total cost is {total_cost} dollars\n"
              f"See you again!\n")
