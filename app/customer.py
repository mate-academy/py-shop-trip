from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_card: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_card
        self.location = location
        self.money = money
        self.car = car

    def count_money(self) -> str:
        return f"{self.name} has {self.money} dollars"

    def distance(self, shop: Shop) -> float:
        point_x = (shop.location[0] - self.location[0]) ** 2
        point_y = (shop.location[1] - self.location[1]) ** 2
        return (point_x + point_y) ** 0.5

    def fare(self, shop: Shop, fuel_price: float) -> float:
        return 2 * (self.distance(shop) * self.car.cost_km() * fuel_price)

    def cost_product(self, shop: Shop) -> dict:
        return {
            shop.name: {
                key: (value * self.product_cart[key])
                for key, value in shop.products.items()
            }
        }

    def product_price(self, shop: Shop) -> dict:
        return {
            shop: sum(products.values())
            for shop, products in self.cost_product(shop).items()
        }

    def total_cost(self, shops: list, fuel_price: float) -> dict:
        dict_cost_trip = {}
        for shop in shops:
            product = self.product_price(shop)[shop.name]
            fuel = self.fare(shop, fuel_price)
            cost_trip = {
                shop.name: round(product + fuel, 2)
            }
            dict_cost_trip.update(cost_trip)
        return dict_cost_trip

    def min_total_cost(self, shops: list, fuel_price: float) -> str:
        min_cost_trip = min(self.total_cost(shops, fuel_price).values())
        for key, value in self.total_cost(shops, fuel_price).items():
            if value != min_cost_trip:
                continue
            return key

    def remainder(
            self,
            shops: list,
            fuel_price: float,
            min_trip: str
    ) -> int:
        return self.money - self.total_cost(shops, fuel_price)[min_trip]
