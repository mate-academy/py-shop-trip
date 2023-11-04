from datetime import datetime


class Shop:
    def __init__(self,
                 name: str,
                 location: list[int],
                 products: dict[str, float],
                 ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def check_prices(self, prod_cart: dict[str, int]) -> float:
        return sum(self.products[prod] * qty
                   for prod, qty in prod_cart.items())

    def sell_products(self, name: str, prod_cart: dict[str, int]) -> str:

        sell_time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        products_lines = [
            f"{qty} {prod}s for {self.products[prod] * qty:g} dollars\n"
            for prod, qty in prod_cart.items()
        ]

        check_lines = [
            f"Date: {sell_time}\n",
            f"Thanks, {name}, for your purchase!\n",
            "You have bought: \n",
            *products_lines,
            f"Total cost is {self.check_prices(prod_cart)} dollars\n",
            "See you again!\n"
        ]

        return "".join(check_lines)
