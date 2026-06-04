import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_product_cost(self, product_cart: dict) -> float:
        return sum(
            count * self.products[product]
            for product, count in product_cart.items()
        )

    def print_recipe(self, customer_name: str, product_cart: dict) -> None:
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer_name}, for your purchase!\n"
            "You have bought:"
        )

        for product, amount in product_cart.items():
            product_total = round(self.products[product] * amount, 2)
            if product_total.is_integer():
                product_total = int(product_total)
            print(f"{amount} {product}s for {product_total} dollars")

        total_cost = round(self.get_product_cost(product_cart), 2)
        if total_cost.is_integer():
            total_cost = int(total_cost)

        print(f"Total cost is "
              f"{total_cost} dollars")
        print("See you again!")
