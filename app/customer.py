from app.car import Car
from app.shop import Shop
from typing import List, Union


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

    def journey_cost(self, shop: Shop) -> float:
        point_x = shop.location[0] - self.location[0]
        point_y = shop.location[1] - self.location[1]
        distance = (point_x ** 2 + point_y ** 2) ** 0.5
        distance_cost = self.car.fuel_cost_calculation_per_distance(distance)
        return distance_cost

    def calc_ult_shopping_journey_cost(self, shop: Shop) -> dict:
        total_sum = shop.calc_cost_of_prod_cart(self) + self.journey_cost(shop)
        return {shop.name: total_sum}

    def display_shop_journey(self, shops: List[Shop]) -> None:
        print(f"{self.name} has {self.money} dollars")

        ult_journ_cost_var_shops = {}
        cheapest_shop_name = ""

        for shop in shops:
            journey_cost_for_shop = self.calc_ult_shopping_journey_cost(shop)
            ult_journ_cost_var_shops.update(journey_cost_for_shop)

            print(f"{self.name}'s trip to the {shop.name} costs "
                  f"{ult_journ_cost_var_shops.get(shop.name):.2f}")

            for shop_name, trip_cost in journey_cost_for_shop.items():
                if trip_cost < \
                        ult_journ_cost_var_shops.get(shop_name, float("inf")):
                    ult_journ_cost_var_shops[shop_name] = trip_cost

            if cheapest_shop_name == "" or \
                    ult_journ_cost_var_shops[shop.name] < \
                    ult_journ_cost_var_shops[cheapest_shop_name]:
                cheapest_shop_name = shop.name

        cheapest_trip_cost = min(ult_journ_cost_var_shops.values())
        cheapest_shop = next(
            (shop for shop in shops if shop.name == cheapest_shop_name), None
        )

        if self.money < cheapest_trip_cost:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return

        print(f"{self.name} rides to {cheapest_shop.name}\n")
        cheapest_shop.shop_purchase_reflect(self)
        print(f"{self.name} rides home")

        remaining_money = self.money - cheapest_trip_cost
        print(f"{self.name} now has {remaining_money:.2f} dollars\n")
