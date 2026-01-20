import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_receipt(
            self,
            customer_name: str,
            customer_product_cart: dict
    ) -> None:
        total_cost = 0
        print(
            f"Date: {datetime.datetime.now():%d/%m/%Y %H:%M:%S}\n"
            f"Thanks, {customer_name}, for your purchase!\n"
            f"You have bought:"
        )
        for product, amount in customer_product_cart.items():
            product_price = amount * self.products[product]
            if product_price == int(product_price):
                product_price = int(product_price)

            print(
                f"{amount} {product}s for {product_price} dollars"
            )
            total_cost += product_price
        print(
            f"Total cost is {total_cost} dollars\n"
            f"See you again!\n"
        )
