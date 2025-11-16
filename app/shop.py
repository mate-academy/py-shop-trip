"""Module for representing shops and products."""
from dataclasses import dataclass, make_dataclass, fields
from typing import TypeVar, Generic, Callable
import datetime
from decimal import Decimal

from app.navigation import Location


T = TypeVar("T")


def make_products(
        product_dict: dict,
        name: str = "Products"
) -> T:
    """
    Create a dataclass for products from a dictionary.

    :param product_dict: A dictionary of products and their prices.
    :type product_dict: dict
    :param name: The name of the dataclass to create.
    :type name: str
    :return: An instance of the created dataclass.
    :rtype: T
    """
    return make_dataclass(
        name,
        [
            (product, type(value))
            for product, value in product_dict.items()
        ]
    )(**product_dict)


@dataclass
class Shop(Generic[T]):
    """Represents a shop with a name, location, and products."""

    name: str
    location: Location
    products: T

    def get_shopping_cost(self, product_cart: T) -> tuple[Decimal, str]:
        """
        Calculate the total cost of a shopping cart and generate a log.

        :param product_cart: The customer's shopping cart.
        :type product_cart: T
        :return: A tuple containing the total cost and the shopping log.
        :rtype: tuple[Decimal, str]
        """
        total_cost = Decimal("0.00")
        shopping_log = ""
        for field in fields(product_cart):
            prod_amount = Decimal(str(getattr(product_cart, field.name)))
            prod_price = Decimal(str(getattr(self.products, field.name, 0)))
            prod_cost = prod_amount * prod_price

            total_cost += prod_cost
            shopping_log += "".join((
                f"{prod_amount} ",
                f"{field.name}{"s" if prod_amount > 1 else ""} ",
                f"for {prod_cost.normalize()} dollars\n"
            ))

        return total_cost, shopping_log

    @staticmethod
    def make_purchase(
            customer_name: str,
            pay: Callable[[Decimal], None],
            shopping_cost: Decimal,
            shopping_log: str
    ) -> None:
        """
        Process a purchase, print a receipt, and deduct payment.

        :param customer_name: The name of the customer.
        :type customer_name: str
        :param pay: A callable to process the payment.
        :type pay: Callable[[Decimal], None]
        :param shopping_cost: The total cost of the shopping.
        :type shopping_cost: Decimal
        :param shopping_log: The log of items purchased.
        :type shopping_log: str
        """
        pay(shopping_cost)
        print("".join([
            f"Date: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n",
            f"Thanks, {customer_name}, for your purchase!\n",
            "You have bought:",
            f"\n{shopping_log}",
            f"Total cost is {shopping_cost.normalize()} dollars\n",
            "See you again!\n"
        ]))
