from dataclasses import dataclass
from app.shop import Shop
from typing import List


@dataclass
class Customer:
    argus: dict
    name: str = None
    product_cart: dict = None
    location: list = None
    money: int | float = None
    car: dict = None
    cheapest_shop: Shop | None = None

    def init_attrs(self) -> None:
        for key, value in self.argus.items():
            setattr(self, key, value)

    def find_cheapest_shop(self, shops: List[Shop]) -> None:
        shops_trip_costs = []
        for shop in shops:
            shop.init_attrs()
            shop.get_cost_of_trip(self.product_cart,
                                  self.location,
                                  self.car)
            print(f"{self.name}\'s trip to the {shop.name} "
                  f"costs {shop.cost_of_trip}")
            shops_trip_costs.append({
                "shop": shop,
                "cost": shop.cost_of_trip
            })
        cheapest_shop_dict = min(shops_trip_costs, key=lambda x: x["cost"])
        if cheapest_shop_dict["cost"] <= self.money:
            self.cheapest_shop = cheapest_shop_dict["shop"]

    def make_a_purchase(self) -> None:
        print(f"{self.name} rides to {self.cheapest_shop.name}\n")
        self.cheapest_shop.print_receipt(self.name, self.product_cart)
        print(f"{self.name} rides home")
        self.money -= self.cheapest_shop.cost_of_trip
        print(f"{self.name} now has {self.money} dollars\n")
