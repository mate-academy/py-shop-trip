from dataclasses import dataclass

from app.car import Car
from app.location import Location


@dataclass
class Customer:
    name: str
    product_cart: dict[str, float]
    location: Location
    money: float
    car: Car

    def __post_init__(self) -> None:
        self.home_location = self.location

    @property
    def rounded_money(self) -> float:
        return round(self.money, 2)

    def calculate_cost_for_ride_to(
            self,
            location: Location,
            fuel_price: float
    ) -> float:
        if self.location == location:
            return 0
        distance = location - self.location
        fuel_consumption_for_km = self.car.fuel_consumption / 100
        cost = distance * fuel_consumption_for_km * fuel_price
        return cost

    def ride_to(
            self,
            location: Location,
            fuel_price: float
    ) -> None:
        if self.location == location:
            return
        ride_cost = self.calculate_cost_for_ride_to(location, fuel_price)
        self.money -= ride_cost
        self.location = location

    def ride_to_shop(
            self,
            shop_name: str,
            shop_location: Location,
            fuel_price: float
    ) -> None:
        self.ride_to(shop_location, fuel_price)
        print(f"{self.name} rides to {shop_name}")

    def ride_home(self, fuel_price: float) -> None:
        self.ride_to(self.home_location, fuel_price)
        print(f"{self.name} rides home")


def convert_customer_from_dict(customer: dict) -> Customer:
    name = customer["name"]
    product_cart = customer["product_cart"]
    location = Location(*customer["location"])
    money = customer["money"]
    car = Car(**customer["car"])
    return Customer(
        name,
        product_cart,
        location,
        money,
        car
    )
