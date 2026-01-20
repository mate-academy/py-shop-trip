import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def total_cost_of_products(self, product_cart: dict) -> float:
        total_cost = 0
        for product in product_cart:
            total_cost += self.products[product] * product_cart[product]
        return total_cost

    def print_receipt(self, customer_name: str, product_cart: dict) -> str:
        total_cost = self.total_cost_of_products(product_cart)
        datetime_now = datetime.datetime.now()
        purchase_date_and_time = datetime_now.strftime("%d/%m/%Y %H:%M:%S")
        products_info = ""

        for product, quantity in product_cart.items():
            product_cost = self.products[product] * quantity
            if product_cost.is_integer():
                formatted_cost = int(product_cost)
            else:
                formatted_cost = product_cost
            products_info += (f"{quantity} {product}s "
                              f"for {formatted_cost} dollars\n")

        return (f"Date: {purchase_date_and_time}\n"
                f"Thanks, {customer_name}, for your purchase!\n"
                f"You have bought:\n"  # noqa: E231
                f"{products_info}"
                f"Total cost is {total_cost} dollars\n"
                f"See you again!\n")
