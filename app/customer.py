from typing import Dict, Any, List
import math
from decimal import Decimal, ROUND_HALF_UP
from app.car import Car
from app.shop import Shop, format_money


def distance(loc1: List[float], loc2: List[float]) -> float:
    dx = loc1[0] - loc2[0]
    dy = loc1[1] - loc2[1]
    return math.hypot(dx, dy)


class Customer:
    def __init__(self, data: Dict[str, Any]) -> None:
        self.name: str = data["name"]
        self.product_cart: Dict[str, int] = data["product_cart"]
        self.location: List[float] = data["location"]
        self.money: float = data["money"]
        self.car: Car = Car(data["car"])
        self.home: List[float] = data["location"][:]

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        d_to_shop = Decimal(str(distance(self.location, shop.location)))
        d_home = Decimal(str(distance(shop.location, self.home)))

        fuel = self.car.fuel_cost(d_to_shop + d_home, fuel_price)
        products = shop.total_cost(self.product_cart)

        total = (fuel + products).quantize(Decimal("0.01"), ROUND_HALF_UP)
        return float(total)

    def choose_shop(self, shops: List[Shop], fuel_price: float) -> Shop:
        shop_costs = []

        for shop in shops:
            cost = self.trip_cost(shop, fuel_price)
            shop_costs.append({"shop": shop, "cost": cost})
            print(f"{self.name}'s trip to the {shop.name} costs {cost:.2f}")

        affordable = [sc for sc in shop_costs if sc["cost"] <= self.money]

        if not affordable:
            return None

        cheapest = min(affordable, key=lambda x: x["cost"])
        return cheapest["shop"]

    def ride_and_buy(self, shop: Shop, fuel_price: float) -> None:
        trip_to_shop = distance(self.location, shop.location)
        trip_home = distance(shop.location, self.home)

        fuel_cost_trip = self.car.fuel_cost(trip_to_shop
                                            + trip_home, fuel_price)
        product_cost = shop.total_cost(self.product_cart).quantize(
            Decimal("0.01"), ROUND_HALF_UP
        )
        total_cost = (fuel_cost_trip + product_cost).quantize(
            Decimal("0.01"), ROUND_HALF_UP
        )

        print(f"{self.name} rides to {shop.name}")

        self.location = shop.location[:]
        shop.receipt(self.name, self.product_cart)

        print(f"{self.name} rides home")
        self.location = self.home[:]

        self.money = float(
            (Decimal(str(self.money)) - total_cost).quantize(
                Decimal("0.01"), ROUND_HALF_UP
            )
        )

        print(f"{self.name} now has {format_money(self.money)} dollars\n")
