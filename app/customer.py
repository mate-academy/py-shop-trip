"""Module for representing customers and their decisions."""
from dataclasses import dataclass, field
from typing import TypeVar, Generic
from decimal import Decimal

from app.navigation import Car, Location
from app.shop import Shop


T = TypeVar("T")


@dataclass
class Decision:
    """Represents a customer's decision to visit a shop."""

    origin: Location
    target: Shop
    trip_cost: Decimal
    shopping_cost: Decimal
    shopping_log: str
    budget_history: list = field(default_factory=list)

    @property
    def total_cost(self) -> Decimal:
        """Calculate the total cost of the trip, including shopping."""
        return (self.trip_cost * 2 + self.shopping_cost).quantize(
            Decimal("0.01")
        )


@dataclass
class Customer(Generic[T]):
    """Represents a customer in the shopping simulation."""

    name: str
    product_cart: T
    location: Location
    money: Decimal
    car: Car
    decision: Decision | None = None

    def spend_money(self, expenses: Decimal) -> None:
        """
        Deduct expenses from the customer's money.

        :param expenses: The amount of money to deduct.
        :type expenses: Decimal
        """
        self.decision.budget_history.append(self.money)
        self.money -= expenses

    def make_decision(
            self,
            fuel_price: Decimal,
            shops: list[Shop[T]]
    ) -> None:
        """
        Make a decision on which shop to visit based on cost.

        :param fuel_price: The current price of fuel.
        :type fuel_price: Decimal
        :param shops: A list of available shops.
        :type shops: list[Shop[T]]
        """
        variants = list()
        for shop in shops:
            trip_cost = self.car.get_trip_cost(
                fuel_price,
                self.location.get_distance(shop.location)
            )
            shopping_cost, shopping_log = shop.get_shopping_cost(
                self.product_cart
            )

            variants.append(
                Decision(
                    origin=self.location,
                    target=shop,
                    trip_cost=trip_cost,
                    shopping_cost=shopping_cost,
                    shopping_log=shopping_log
                )
            )
            print(
                f"{self.name}'s trip to the",
                f"{shop.name} costs {variants[-1].total_cost}"
            )

        if (
            decision := min(
                variants,
                key=lambda d: d.total_cost
            )
        ).total_cost <= self.money:
            self.decision = decision
            return

        print(
            f"{self.name} doesn't have enough money "
            "to make a purchase in any shop"
        )

    def budget_log(self, end_line: bool = False) -> None:
        """
        Log the customer's current budget.

        :param end_line: Whether to print a newline at the end.
        :type end_line: bool
        """
        message = [
            self.name,
            "has",
            str(self.money.quantize(Decimal("0.01")).normalize()),
            "dollars"
        ]
        if (
            self.decision
            and self.money != self.decision.budget_history[-1]
        ):
            message.insert(1, "now")

        print(" ".join(message))
        if end_line:
            print()

    def change_location(self) -> None:
        """Change the customer's location based on their decision."""
        if not self.decision:
            return

        self.spend_money(self.decision.trip_cost)

        if self.location == self.decision.origin:
            self.location = self.decision.target.location
            print(f"{self.name} rides to {self.decision.target.name}\n")
            return

        self.location = self.decision.origin
        print(f"{self.name} rides home")
