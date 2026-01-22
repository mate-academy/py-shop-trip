from typing import List, TYPE_CHECKING
from app.car import Car


if TYPE_CHECKING:
    from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[int],
        money: int,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def __repr__(self) -> str:
        return (
            f"Customer ({self.name}, {self.product_cart}, "
            f"{self.location}, {self.money}, {self.car})"
        )

    def travel_to_shop(
        self,
        shop: "Shop",
        fuel_price: float
    ) -> float:
        return 2 * self.car.trip_cost(
            self.location,
            shop.location,
            fuel_price
        )

    def make_purchase(self, shop: "Shop") -> float:

        return sum(
            price * self.product_cart[name]
            for name, price in shop.products.items()
        )

    def find_cheapest_shop(
        self,
        shops: List["Shop"],
        fuel_price: float
    ) -> None:
        cheapest_shop = None
        min_cost = float("inf")
        print(f"{self.name} has {self.money} dollars")

        for shop in shops:
            total_cost = round(
                self.make_purchase(shop)
                + self.travel_to_shop(shop, fuel_price),
                2
            )

            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")
            if total_cost <= min_cost and total_cost <= self.money:
                cheapest_shop = shop
                min_cost = total_cost
        if cheapest_shop:
            print(f"{self.name} rides to {cheapest_shop.name}\n")
            self.money = round(self.money - min_cost, 2)
            cheapest_shop.check(self)
            print(
                f"{self.name} rides home\n"
                f"{self.name} now has {self.money} dollars\n"
            )

        else:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
