import json
from typing import Any, cast, TYPE_CHECKING
import datetime

from app.customer import format_price

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    """Represents a shop with its details."""

    def __init__(
            self,
            name: str,
            location: list[float],
            products: dict[str, float],
    ) -> None:
        """
        Initializes a Shop instance.

        Args:
            name: The shop's name.
            location: The shop's coordinates [x, y].
            products: A dictionary of products and their prices.
        """
        self.name = name
        self.location = location
        self.products = products

    def print_purchase_receipt(self, customer: "Customer",
                               shopping_cost: float) -> None:
        """
        Prints the purchase receipt for a customer's shopping trip.

        Args:
            customer: The customer making the purchase.
            shopping_cost: Pre-calculated cost of products.
        """
        time_format = "%d/%m/%Y %H:%M:%S"
        print(f"Date: {datetime.datetime.now().strftime(time_format)}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for product, quantity in customer.product_cart.items():
            unit_price = self.products[product]
            total_price = unit_price * quantity
            plural = "s" if quantity > 1 else ""
            print(
                f"{quantity} {product}{plural} for "
                f"{format_price(total_price)} dollars"
            )

        print(f"Total cost is {format_price(shopping_cost)} dollars")
        print("See you again!")


class ShopManager:
    """Manages loading shop and customer data from a configuration file."""

    def __init__(self, config_path: str = "app/config.json") -> None:
        """
        Initializes the ShopManager by loading data from the config file.

        Args:
            config_path: The path to the JSON configuration file.
        """
        from app.customer import Customer

        with open(config_path, "r") as f:
            config: dict[str, Any] = json.load(f)

        self.fuel_price: float = config["FUEL_PRICE"]
        self.shops: list[Shop] = [
            Shop(
                name=shop_data["name"],
                location=shop_data["location"],
                products=shop_data["products"],
            )
            for shop_data in config["shops"]
        ]
        self.customers: list[Customer] = [
            Customer(
                name=cust_data["name"],
                product_cart=cust_data["product_cart"],
                location=cust_data["location"],
                money=cust_data["money"],
                car_data=cust_data["car"],
            )
            for cust_data in cast(list[dict[str, Any]], config["customers"])
        ]
