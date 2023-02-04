from app.customer import Customer
from datetime import datetime
from math import sqrt


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
        self.price = 0

    def calculation_distance_to_shop(self, other: Customer) -> float:
        distance = round(sqrt(
            (self.location[0] - other.location[0]) ** 2
            + (self.location[1] - other.location[1]) ** 2), 2)
        return distance

    def calculation_cost_basket_products(self, other: Customer) -> int:
        self.price = (
            self.products["milk"] * other.product_cart["milk"]
            + self.products["bread"] * other.product_cart["bread"]
            + self.products["butter"] * other.product_cart["butter"]
        )
        return self.price

    def what_customer_bought(self, customer: Customer) -> str:
        today = datetime.today().strftime("%d/%m/%Y %H:%M:%S")
        milk_cost = customer.product_cart["milk"] * self.products["milk"]
        bread_cost = customer.product_cart["bread"] * self.products["bread"]
        butter_cost = customer.product_cart["butter"] * self.products["butter"]
        return (
            f"Date: {today}\n"
            f"Thanks, {customer}, for you purchase!\n"
            f"You have bought:\n"
            f"{customer.product_cart['milk']} milks for "
            f"{milk_cost} dollars\n"
            f"{customer.product_cart['bread']} breads for "
            f"{bread_cost} dollars\n"
            f"{customer.product_cart['butter']} butters for "
            f"{butter_cost} dollars\n"
            f"Total cost is {self.price} dollars\n"
            f"See you again!"
        )
