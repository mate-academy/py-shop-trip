import datetime


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        shop_receipt = (f"Date: {current_date}\n"
                        f"Thanks, {customer_name}, for your purchase!\n"
                        "You have bought:\n")

        money_total = 0
        for product, count in product_cart.items():
            product_cost = count * self.products[product]
            if product_cost == int(product_cost):
                product_cost = int(product_cost)
            money_total += product_cost
            shop_receipt += f"{count} {product}s for {product_cost} dollars\n"
        shop_receipt += (f"Total cost is {money_total} dollars\n"
                         "See you again!\n")
        print(shop_receipt)
