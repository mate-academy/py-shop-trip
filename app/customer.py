import math
from typing import Any, TYPE_CHECKING

from app.car import Car

if TYPE_CHECKING:
    from app.shop import Shop


def format_price(price: float) -> str:
    """
    Format price to match expected output.
    Shows integers without decimal places, floats with decimal places.
    """
    if price == int(price):
        return str(int(price))
    else:
        return str(round(price, 2))


class Customer:
    """Represents a customer with their details and shopping logic."""

    def __init__(
            self,
            name: str,
            location: list[float],
            product_cart: dict[str, int],
            money: float,
            car_data: dict[str, Any],
    ) -> None:
        """
        Initializes a Customer instance.

        Args:
            name: The customer's name.
            location: The customer's coordinates [x, y].
            product_cart: A dictionary of products and quantities to buy.
            money: The amount of money the customer has.
            car_data: A dictionary with car details.
        """
        self.name = name
        self.location = location
        self.product_cart = product_cart
        self.money = money
        self.car = Car(
            brand=car_data["brand"],
            fuel_consumption=car_data["fuel_consumption"],
        )

    def calculate_trip_cost(
            self, shops: list["Shop"], fuel_price: float
    ) -> list[tuple[str, float, float]]:
        """
        Calculates the total cost of a shopping trip to each given shop.

        The total cost includes the fuel for a round trip and the cost of
        all products in the shopping cart.

        Args:
            shops: A list of shops to calculate the trip cost for.
            fuel_price: The price of one liter of fuel.

        Returns:
            A list of tuples, where each tuple contains the shop's name,
            the total calculated cost of the trip, and the shopping cost.
        """
        trip_options: list[tuple[str, float, float]] = []
        for shop in shops:
            # Check if shop has all required products
            if not all(product in shop.products
                       for product in self.product_cart):
                continue  # Skip this shop as it's not a valid option

            # Calculate Euclidean distance between customer and shop.
            distance = math.hypot(
                shop.location[0] - self.location[0],
                shop.location[1] - self.location[1]
            )

            # Calculate the cost of all products in the cart for the shop.
            shopping_cost = sum(
                quantity * shop.products[product]
                for product, quantity in self.product_cart.items()
            )

            # Calculate fuel cost for a round trip (to the shop and back).
            fuel_cost = ((distance * 2)
                         * (self.car.fuel_consumption / 100) * fuel_price)

            total_trip_cost = shopping_cost + fuel_cost
            trip_options.append((shop.name, total_trip_cost, shopping_cost))

        return trip_options
