import datetime


class Shop:
    def __init__(self, shop_data: dict) -> None:
        self.name = shop_data["name"]
        self.location = shop_data["location"]
        self.products = shop_data["products"]

    def find_shopping_cost(self, product_cart: dict) -> float:
        shopping_cost = sum(
            product_cart[product] * self.products[product]
            for product in product_cart
        )
        return shopping_cost

    def print_receipt(self, name: str, product_cart: dict) -> None:
        print(
            f"Date: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {name}, for your purchase!\n"
            f"You have bought:"
        )
        shopping_cost = self.find_shopping_cost(product_cart)
        for key, value in product_cart.items():
            product_cost = value * self.products[key]
            if product_cost % 1 == 0:
                product_cost = int(product_cost)
            print(
                f"{value} {key}s for "
                f"{product_cost} dollars"
            )
        print(
            f"Total cost is {shopping_cost} dollars\n"
            f"See you again!\n"
        )
