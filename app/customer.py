from app.car import Car
from app.shop import Shop
from app.utils import calculate_distance


class Customer:
    """
    Represents a customer who wants to make a shopping trip.
    """

    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: list[int],
        money: float,
        car_data: dict,
        fuel_price: float
    ) -> None:
        """
        :param name: Customer's name.
        :param product_cart: Products and quantities to buy.
        :param location: Customer's [x, y] location.
        :param money: Available money.
        :param car_data: Dictionary containing car brand and fuel consumption.
        :param fuel_price: Price for 1 liter of fuel.
        """
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.initial_location = location[:]
        self.money = money
        self.car = Car(car_data["brand"], car_data["fuel_consumption"])
        self.fuel_price = fuel_price

    def calculate_fuel_cost(self, distance: float) -> float:
        """
        Calculates the fuel cost for a given distance.
        """
        fuel_needed = (distance / 100.0) * self.car.fuel_consumption
        return fuel_needed * self.fuel_price

    def _compute_trip_costs(self, shop: Shop) -> dict:
        """
        Computes all distances and fuel costs needed for the trip.
        Shared logic for both calculate_total_trip_cost and ride_to_shop.
        """
        distance_to_shop = calculate_distance(
            self.initial_location,
            shop.location
        )

        fuel_cost_one_way = self.calculate_fuel_cost(distance_to_shop)
        fuel_cost_home = fuel_cost_one_way  # same distance back

        products_cost = shop.get_products_cost(self.product_cart)

        return {
            "distance": distance_to_shop,
            "fuel_cost_one_way": fuel_cost_one_way,
            "fuel_cost_home": fuel_cost_home,
            "products_cost": products_cost,
        }

    def calculate_total_trip_cost(self, shop: Shop) -> float:
        """
        Calculates the total cost of the round trip (fuel to
            shop + products + fuel back).
        """
        costs = self._compute_trip_costs(shop)

        total_cost = (
            costs["fuel_cost_one_way"]
            + costs["products_cost"]
            + costs["fuel_cost_home"]
        )

        return round(total_cost, 2)

    def ride_to_shop(self, shop: Shop) -> None:
        """
        Customer rides to the shop, makes a purchase, and returns home.
        """
        print(f"{self.name} rides to {shop.name}")

        costs = self._compute_trip_costs(shop)

        self.money -= costs["fuel_cost_one_way"]
        self.location = shop.location[:]

        products_cost = shop.print_receipt(self.name, self.product_cart)
        self.money -= products_cost

        print(f"{self.name} rides home")

        self.money -= costs["fuel_cost_home"]
        self.location = self.initial_location[:]

        print(f"{self.name} now has {self.money:.2f} dollars\n")
