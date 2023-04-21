from app.car import Car
from app.shop import Shop
from typing import Union


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[int],
        money: Union[int, float],
        car: dict,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.distance_to_shop = 0
        self.money = money
        self.car: Car = Car(**car)
        self.closest_shop_by_distance_cost = {}
        self.ultimate_journey_cost_different_shops = {}

    def journey_cost(self, shop: Shop) -> int:
        point_x = shop.location[0] - self.location[0]
        point_y = shop.location[1] - self.location[1]
        distance = (point_x ** 2 + point_y ** 2) ** 0.5
        distance_cost = self.car.fuel_cost_calculation_per_distance(distance)

        products_cost = 0
        for product, amount in self.product_cart.items():
            products_cost += shop.products[product] * amount

        return distance_cost + products_cost

    def calculates_ultimate_shopping_journey_cost(self, shops: list[Shop]) -> None:
        for shop in shops:
            self.ultimate_journey_cost_different_shops[shop.name] = (
                    shop.calculates_cost_of_product_cart(self)
                    + self.journey_cost(shop)
            )

    def render_shop_journey(self) -> None:
        print(f"{self.name} has {self.money:.2f} dollars")

        for shop_name, trip_cost in self.ultimate_journey_cost_different_shops.items():
            print(f"{self.name}'s trip to {shop_name} costs {trip_cost:.2f}")

        cheapest_trip_cost = min(self.ultimate_journey_cost_different_shops.values())
        cheapest_shop_name = ""

        for shop_name, trip_cost in self.ultimate_journey_cost_different_shops.items():
            if trip_cost == cheapest_trip_cost:
                cheapest_shop_name = shop_name
                break

        for shop in Shop.shops:
            if shop.name == cheapest_shop_name:
                cheapest_shop = shop
                break

        if self.money < cheapest_trip_cost:
            print(f"{self.name} doesn't have enough money to make a purchase in any shop")
            return

        print(f"{self.name} rides to {cheapest_shop.name}")
        cheapest_shop.shop_purchase_reflect(self)
        print(f"{self.name} rides home")

        remaining_money = self.money - cheapest_trip_cost
        print(f"{self.name} now has {remaining_money:.2f} dollars")
