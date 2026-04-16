import datetime

from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict,
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_check(
            self,
            cust: Customer,
    ) -> None:
        milk = cust.product_cart["milk"] * self.products["milk"]
        bread = cust.product_cart["bread"] * self.products["bread"]
        butter = cust.product_cart["butter"] * self.products["butter"]
        result = milk + bread + butter
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {cust.name}, for your purchase!\n"
            f"You have bought:\n"
            f"{cust.product_cart['milk']} milks for {round(milk)} dollars\n"
            f"{cust.product_cart['bread']} breads for {round(bread)} dollars\n"
            f"{cust.product_cart['butter']} butters for {butter} dollars\n"
            f"Total cost is {result} dollars\n"
            f"See you again!\n"
        )
