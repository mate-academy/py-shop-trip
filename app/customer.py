from app.car import Car
from app.shop import Shop
from app.utils import get_distance


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float,
            car_data: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(
            brand=car_data["brand"],
            fuel_consumption=car_data["fuel_consumption"]
        )
        self.home_location = location.copy()

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        one_way = get_distance(self.home_location, shop.location)
        round_trip = one_way * 2
        return self.car.calculate_fuel_cost(round_trip, fuel_price)

    def full_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        fuel_cost = self.calculate_trip_cost(shop, fuel_price)
        product_cost = shop.calculate_cart_cost(self.product_cart)
        return fuel_cost + product_cost

    def ride_to(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        print()
        self.location = shop.location.copy()

    def ride_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = self.home_location.copy()

    def buy_products(self, shop: Shop, fuel_price: float) -> None:
        cost = self.full_trip_cost(shop, fuel_price)
        self.money -= cost
        shop.print_receipt(self, self.product_cart)
