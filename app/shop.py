import dataclasses
import math


@dataclasses.dataclass
class Shop:
    name: str
    location: list
    products: dict
    products_price: float = 0
    trip_price: float = 0

    def count_trip_price(self, other: object, fuel_price: float) -> object:
        self.products_price = sum(
            [
                self.products[product] * count
                for product, count in other.product_cart.items()
            ]
        )
        distance = math.dist(self.location, other.location)
        ride_price = 2 * fuel_price * (distance
                                       * other.car["fuel_consumption"] / 100)
        self.trip_price = round(ride_price + self.products_price, 2)
        print(f"{other.name}'s trip to the "
              f"{self.name} costs {self.trip_price}")
        return self
