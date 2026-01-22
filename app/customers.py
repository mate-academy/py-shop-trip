from dataclasses import dataclass
from app.shops import Shop


@dataclass
class Car:
    brand: str
    consumption: float


@dataclass
class Customer:
    name: str
    products: dict
    location: list
    money: float
    car: Car

    def calculate_trip_cost(self,
                            shop: Shop,
                            fuel_cost: float) -> float:
        distance = ((abs((self.location[0] - shop.location[0]) ** 2)
                     + abs((self.location[1]
                            - shop.location[1]) ** 2))) ** 0.5 * 2
        cost = round(self.car.consumption * distance * fuel_cost / 100, 2)
        return cost

    def shopping_cost(self, shop: Shop) -> dict:
        total_cost = 0
        purchases = {}
        for product in self.products.items():
            item_cost = shop.products.get(product[0]) * product[1]
            if int(item_cost) == item_cost:
                purchases[f"{product[1]} {product[0]}s for "] = int(item_cost)
            else:
                purchases[f"{product[1]} {product[0]}s for "] = item_cost
            total_cost += item_cost
        purchases["Total cost is "] = total_cost
        return purchases
