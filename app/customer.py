from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[int],
        money: int | float,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home = self.location

    def plan_trip(
        self, shops_list: list[Shop], fuel_price: float
    ) -> tuple | None:
        costs: list = []
        for shop in shops_list:
            ride_cost = (
                self.car.ride_cost(self.location, shop.location, fuel_price)
                * 2
            )
            shopping_cost = sum(
                self.product_cart[prod] * shop.products[prod]
                for prod in self.product_cart
            )
            total = ride_cost + shopping_cost
            print(
                f"{self.name}'s trip to the "
                f"{shop.name} costs {round(total, 2)}"
            )
            costs.append((shop, total, ride_cost))
        min_cost_shop: tuple = min(costs, key=lambda x: x[1])
        if min_cost_shop[1] > self.money:
            return None
        return min_cost_shop

    def ride_to(self, destination: Shop, ride_cost: float) -> None:
        print(f"{self.name} rides to {destination.name}\n")
        self.money -= ride_cost
        self.location = destination.location

    def ride_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = self.home
