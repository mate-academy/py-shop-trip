import math
from app.car import Car
from app.shop import Shop


class Customer:
    """Represents a customer who travels and makes purchases."""

    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: list[int],
            money: float,
            car: dict[str, str | float]
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self._location = location
        self.money = money
        self.car = Car.setup_car(car, location)
        self.cheapest_shop = None
        self.cheapest_cost = 0

    @property
    def location(self) -> list[int]:
        """Get customer's current location."""
        return self._location

    @location.setter
    def location(
            self,
            location: list[int]
    ) -> None:
        """Set customer's current location."""
        self._location = location

    def return_home(self) -> None:
        """Return to initial home location."""
        self.location = self.car.home_location

    def pay_purchase(
            self,
            bill: float
    ) -> None:
        """Deduct purchase cost from customer's money."""
        self.money -= bill

    def calculate_road_cost(
            self,
            shop_location: list[int],
            fuel_price: float
    ) -> float:
        """Calculate fuel cost to travel to a shop."""
        return (fuel_price
                * self.car.fuel_consumption
                * math.dist(self.location, shop_location)) / 100

    def preparation(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> None:
        """Compare shops, print costs and choose cheapest."""
        print(f"{self.name} has {self.money} dollars")

        results = [
            shop.count_prices(
                self.product_cart,
                self.name,
                self.calculate_road_cost(shop.location, fuel_price),
            )
            for shop in shops
        ]

        cheapest_index = results.index(min(results))
        self.cheapest_shop = shops[cheapest_index]
        self.cheapest_cost = round(results[cheapest_index], 2)
        self.ride_and_make_purchase()

    def ride_and_make_purchase(self) -> None:
        """Travel, purchase, pay, return home."""
        if self.cheapest_cost > self.money:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return

        print(f"{self.name} rides to {self.cheapest_shop.name}")

        self.cheapest_shop.make_purchase(self.name, self.product_cart)
        self.location = self.cheapest_shop.location
        self.pay_purchase(self.cheapest_cost)
        self.ride_home()

    def ride_home(self) -> None:
        """Print go-home action and remaining balance."""
        print(f"{self.name} rides home")
        self.return_home()
        print(f"{self.name} now has {self.money} dollars\n")
