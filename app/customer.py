from app.car import Car
from app.shop import Shop


class Customer:
    customers = []

    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[int],
        money: int | float,
        car: dict,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)
        self.closest_shop_by_distance_cost = {}
        self.full_trip_cost_different_shops = {}
        Customer.customers.append(self)

    def calculates_full_shopping_trip_cost(self, shop: Shop) -> None:
        self.full_trip_cost_different_shops[
            shop.name
        ] = shop.calculates_cost_of_product_cart(
            self
        ) + self.car.calculates_trip_cost_to_shop(
            self, shop
        )

    def display_shop_trip(self) -> None:
        print(f"{self.name} has {self.money} dollars")
        for name, summary in self.full_trip_cost_different_shops.items():
            print(
                f"{self.name}'s trip to the {name} costs {round(summary, 2)}"
            )
        cheapest = min(self.full_trip_cost_different_shops.values())
        cheapest_shop = ""
        for key, value in self.full_trip_cost_different_shops.items():
            if value == cheapest:
                cheapest_shop_name = key
        for shop in Shop.shops:
            if shop.name == cheapest_shop_name:
                cheapest_shop = shop
        if self.money < cheapest:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            return
        print(f"{self.name} rides to {cheapest_shop.name}\n")
        cheapest_shop.shop_purchase_display(self)
        print(f"{self.name} rides home")
        print(
            f"{self.name} now has"
            f" {round(self.money - cheapest, 2)} dollars\n"
        )
