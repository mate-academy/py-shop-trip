from dataclasses import dataclass, field
from app.utils import distance_km
from app.shop import Shop
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    location: list[float]
    money: float
    car: Car
    home_location: list[float] = field(init=False)

    def __post_init__(self) -> None:
        self.home_location = list(self.location)

    def trip_total_cost(self, shop: Shop, fuel_price: float) -> float | None:
        if not shop.can_fulfill(self.product_cart):
            return None

        dist = distance_km(self.home_location, shop.location)
        fuel = self.car.fuel_cost_round_trip(dist, fuel_price)
        items = shop.cart_cost(self.product_cart)
        return fuel + items

    def can_afford(self, total_cost: float) -> bool:
        return self.money >= total_cost

    def ride_to(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = list(shop.location)

    def ride_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = list(self.home_location)

    def pay(self, amount: float) -> None:
        self.money -= amount

    def choose_best_shop(
            self, shops: list[Shop],
            fuel_price: float
    ) -> tuple[Shop, float] | None:
        best: tuple[Shop, float] | None = None

        for shop in shops:
            total = self.trip_total_cost(shop, fuel_price)
            if total is None:
                continue
            if best is None or total < best[1]:
                best = (shop, total)

        return best
