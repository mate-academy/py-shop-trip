from app.shop import Shop
from app.utils import calculate_distance
from app.car import Car


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: float,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home = location.copy()

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = calculate_distance(self.location, shop.location)
        fuel = self.car.fuel_cost(distance, fuel_price)
        return 2 * fuel + shop.products_cost(self.product_cart)

    def ride_to(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = list(shop.location)

    def ride_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = self.home.copy()
