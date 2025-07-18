from __future__ import annotations

from app.car import Car
from app.location import Location
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: Location,
        money: float,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location
        self.money = money
        self.car = car

    def _choose_shop(
        self,
        shops: list[Shop],
        fuel_price: float
    ) -> tuple[float, Shop]:
        print(f"{self.name} has {round(self.money, 2)} dollars")
        min_cost = float("inf")
        best_shop: Shop | None = None

        for shop in shops:
            distance = self.location.distance(shop.location)
            cost = (
                2 * self.car.calculate_cost(distance, fuel_price)
                + shop.calculate_cost(self.product_cart)[0]
            )
            print(
                f"{self.name}'s trip to "
                f"the {shop.name} costs {round(cost, 2)}"
            )

            if min_cost > cost:
                min_cost = cost
                best_shop = shop

        return min_cost, best_shop

    def go_to_shop(self, shops: list[Shop], fuel_price: float) -> bool:
        cost, shop = self._choose_shop(shops, fuel_price)
        if cost > self.money:
            print(
                f"{self.name} doesn't have "
                "enough money to make a purchase in any shop"
            )
            return False
        self.location = shop.location
        print(f"{self.name} rides to {shop.name}")
        shop.print_purchase(self.name, self.product_cart)
        self.money -= cost
        return True

    def go_to_home(self) -> None:
        self.location = self.home_location
        print(f"{self.name} rides home")
        print(f"{self.name} now has {round(self.money, 2)} dollars")
        print()

    def full_trip(self, shops: list[Shop], fuel_price: float) -> None:
        if not self.go_to_shop(shops, fuel_price):
            return
        self.go_to_home()

    def __repr__(self) -> str:
        return (
            "self("
            f"name={self.name}, "
            f"product_cart={self.product_cart}, "
            f"location={self.location}, "
            f"money={self.money}, "
            f"car={self.car}"
            ")"
        )

    def __str__(self) -> str:
        return self.__repr__()

    @classmethod
    def from_dict(cls, data: dict) -> Customer:
        return cls(
            name=data.get("name", ""),
            product_cart=data.get("product_cart", {}),
            location=Location(*data.get("location", [0, 0])),
            money=data.get("money", 0.0),
            car=Car(**data.get("car"))
        )
