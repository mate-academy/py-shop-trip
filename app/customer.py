from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: list[int | float],
        money: int | float,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location.copy()
        self.home_location = location.copy()
        self.money = money
        self.car = car

    def calculate_products_cost(self, shop: Shop) -> float:
        return shop.calculate_cart_cost(product_cart=self.product_cart)

    def calculate_trip_cost(
        self,
        shop: Shop,
        fuel_price: int | float
    ) -> float:
        product_cost = self.calculate_products_cost(shop)
        fuel_cost = self.car.calculate_fuel_cost(
            first=self.location,
            second=shop.location,
            price=fuel_price,
        )
        return product_cost + fuel_cost

    def ride(self, location: list[int | float]) -> None:
        self.location = location.copy()

    def to_house(self) -> None:
        self.location = self.home_location.copy()

    def pay(self, cost: float) -> None:
        self.money -= cost
