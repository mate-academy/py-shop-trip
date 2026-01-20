from typing import Dict, List, Tuple
from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(
        self,
        name: str,
        products: Dict[str, int],
        location: List[float],
        money: float,
        car: Car
    ) -> None:
        self.name: str = name
        self.products: Dict[str, int] = products
        self.location: List[float] = location
        self.money: float = money
        self.car: Car = car

    def get_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def trip_to_shop(
            self, shop: Shop, fuel_price: float
    ) -> Tuple[float, Shop]:
        total_cost: float = 0.0
        fuel_cost = self.car.cost_of_fuel_all_way(
            self.location, shop.location
        ) * fuel_price
        total_cost += fuel_cost
        total_cost += shop.purchase(self.products)
        print(f"{self.name}'s trip to the {shop.name}"
              f" costs {round(total_cost, 2)}")
        return round(total_cost, 2), shop

    def list_of_bought_stuff(self, shop: Shop) -> float:
        total_cost: float = 0.0
        for key, value in self.products.items():
            price: float = shop.products[key] * value
            total_cost += price
            price_display: float | int = int(price) if price % 1 == 0\
                else price
            print(f"{value} {key}s for {price_display} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        return total_cost

    def amount_of_money_after_purchase(self, shop: Shop) -> float:
        return self.money - self.list_of_bought_stuff(shop)
