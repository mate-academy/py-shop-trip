"""Module for simulating a shop trip."""
from decimal import Decimal

from app.customer import Customer
from app.navigation import Location, Car
from app.shop import Shop, make_products


class ShopTrip:
    """Represents a shopping trip simulation."""

    def __init__(self, data: dict) -> None:
        """
        Initialize a ShopTrip instance.

        :param data: A dictionary containing the simulation data.
        :type data: dict
        """
        self.FUEL_PRICE = Decimal(str(data.get("FUEL_PRICE", 1)))
        self.customers = [
            Customer(
                name=customer.get("name", "John"),
                product_cart=make_products(customer.get("product_cart", {})),
                location=Location(*customer.get("location")),
                money=Decimal(str(customer.get("money", 0))),
                car=None if not (car := customer.get("car")) else Car(
                    brand=car.get("brand", "Unknown"),
                    fuel_consumption=Decimal(
                        str(car.get("fuel_consumption", 10))
                    )
                )
            )
            for customer in data.get("customers", [])
        ]
        self.shops = [
            Shop(
                name=shop.get("name", "ATB"),
                location=Location(*shop.get("location")),
                products=make_products(shop.get("products", {}))
            )
            for shop in data.get("shops", [])
        ]

    def run_event(self) -> None:
        """Run the shopping trip simulation event for all customers."""
        for customer in self.customers:
            customer.budget_log()
            customer.make_decision(self.FUEL_PRICE, self.shops)
            customer.change_location()
            if customer.decision:
                customer.decision.target.make_purchase(
                    customer_name=customer.name,
                    pay=customer.spend_money,
                    shopping_cost=customer.decision.shopping_cost,
                    shopping_log=customer.decision.shopping_log
                )
                customer.change_location()
                customer.budget_log(end_line=True)
