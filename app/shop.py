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

    def print_check(
            self,
            customer_name: str,
            customer_cart: dict
    ) -> None:
        sum_ = 0
        check = ""
        for product in customer_cart:
            product_sum = customer_cart[product] * self.products[product]
            product_sum = (
                int(product_sum)
                if product_sum == int(product_sum)
                else product_sum
            )

            check += (
                f""
                f"{customer_cart[product]} {product}s "
                f"for {product_sum} "
                f"dollars\n"
            )
            sum_ += customer_cart[product] * self.products[product]

        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer_name}, for your purchase!\n"
            f"You have bought:\n"
            f"{check}"
            f"Total cost is {sum_} dollars\n"
            f"See you again!\n"
        )
