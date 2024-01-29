from dataclasses import dataclass, field
from app.car import Car, FuelPrice
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int, int]
    money: int
    car: dict | Car = field(default_factory=dict)
    best_shop: dict = None

    def __post_init__(self) -> None:
        self.car = Car(self.car["brand"], self.car["fuel_consumption"])

    def cost_shop(self, shop: Shop) -> float:
        purchase = sum(shop.products[product_customer] * qty
                       for product_customer, qty in self.product_cart.items()
                       if product_customer in shop.products)
        fuel_cost = (self.distance(shop) * self.car.fuel_consumption
                     / 100 * FuelPrice.value * 2)
        cost = round(fuel_cost + purchase, 2)
        print(f"{self.name}'s trip to the {shop.name} costs {cost}")
        return cost

    def choose_shop(self, shops: list[Shop]) -> None:
        index_shop, cost_shop = min(enumerate(map(self.cost_shop, shops)),
                                    key=lambda pair: pair[1])
        if cost_shop > self.money:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return
        self.best_shop = {"link": shops[index_shop], "cost": cost_shop}
        print(f"{self.name} rides to {self.best_shop["link"].name}\n")

    def distance(self, shop: Shop) -> float:
        return ((self.location[0] - shop.location[0]) ** 2
                + (self.location[1] - shop.location[1]) ** 2) ** 0.5
