import datetime


class Shop:
    def __init__(
            self,
            shop_name: str,
            shop_location: list,
            shop_products: dict
    ) -> None:
        self.shop_name = shop_name
        self.shop_location = shop_location
        self.shop_products = shop_products

    def bill(self, customer_name: str, products_needed: dict) -> str:
        out = """"""
        out += (f"Date: "
                f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
                f"\n")
        out += f"Thanks, {customer_name}, for your purchase!\n"
        out += "You have bought:\n"
        total_amount = 0
        for product in self.shop_products:
            total_for_product = (
                products_needed[product]
                * self.shop_products[product]
            )
            total_amount += total_for_product
            if total_for_product == int(total_for_product):
                total_for_product = int(total_for_product)
            out += (f"{products_needed[product]} {product}s "
                    f"for {total_for_product} dollars\n")
        out += f"Total cost is {total_amount} dollars\n"
        out += "See you again!\n"
        return out
