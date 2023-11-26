from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        to_buy: dict,
        location: list[int],
        money: int,
        car: Car

    ) -> None:
        self.name = name
        self.to_buy = to_buy
        self.location = location
        self.money = money
        self.car = car

    def choose_shop(self, shops: list[Shop], fuel_price: float) -> dict:
        cheapest_shop = {}
        for shop in shops:
            product_cost = shop.is_products(self.to_buy)
            travel_cost = self.car.get_travel_cost(
                fuel_price,
                self.location,
                shop.location
            )
            if product_cost:
                print(
                    f"{self.name}'s trip to the {shop.name} "
                    f"costs {round(product_cost + travel_cost * 2, 2)}"
                )
                total_cost = product_cost + travel_cost * 2
                total_cheap_cost = cheapest_shop.get("total_cost")
                if not total_cheap_cost or total_cheap_cost > total_cost:
                    cheapest_shop["total_cost"] = total_cost
                    cheapest_shop["shop"] = shop
        return cheapest_shop
