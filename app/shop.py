import datetime


class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cart_cost(self, product_cart: dict) -> float:
        total_price = 0
        for product in product_cart:
            if product in self.products:
                total_price += product_cart[product] * self.products[product]
        return total_price

    def print_receipt(
            self,
            customer_name: str,
            product_cart: dict,
            total_cost: float
    ) -> None:
        current_date = datetime.datetime.now()
        formatted_date = current_date.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {formatted_date}")
        print(f"Thanks, {customer_name}, for your purchase!\nYou have bought:")
        for product in product_cart:
            product_cost = product_cart[product] * self.products[product]

            if float(product_cost).is_integer():
                product_cost = int(product_cost)
            print(
                f'{product_cart[product]} {product.strip('"')}s for '
                f"{product_cost} dollars"
            )
        print(f"Total cost is {total_cost} dollars\nSee you again!")
        print("")
