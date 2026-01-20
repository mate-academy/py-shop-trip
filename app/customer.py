from dataclasses import dataclass

from app.car import Car
from app.shop import Shop


@dataclass
class Customers:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car

    def __post_init__(self) -> None:
        if isinstance(self.car, dict):
            self.car = Car(**self.car)

    def customers_info(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calculate_distance(self, shop: Shop) -> float:
        return ((self.location[0] - shop.location[0]) ** 2
                + (self.location[1] - shop.location[1]) ** 2) ** 0.5

    def calculate_trip_cost(self, fuel_price: float, shop: Shop) -> float:
        distance = self.calculate_distance(shop)
        fuel_consumption = self.car.fuel_consumption_per_100_km(distance)
        return (fuel_consumption * fuel_price) * 2

    def look_for_cheapest_shop(self,
                               fuel_price: float,
                               shops: list[Shop]
                               ) -> tuple[None | Shop, float, float]:
        cheapest_shop = None
        min_product_cost = None
        min_total_cost = float("inf")

        for shop in shops:
            trip_cost = self.calculate_trip_cost(fuel_price, shop)
            products_cost = shop.calculate_products_cost(self.product_cart)
            total_cost = trip_cost + products_cost
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {round(total_cost, 2)}")

            if total_cost <= self.money and total_cost < min_total_cost:
                cheapest_shop = shop
                min_product_cost = products_cost
                min_total_cost = total_cost

        return cheapest_shop, min_total_cost, min_product_cost

    def make_purchase(self,
                      shop: Shop,
                      total_cost: float,
                      product_cost: float) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location

        shop.prints_check(self.name, self.product_cart, product_cost)
        self.money -= total_cost
        print(f"{self.name} rides home")
        self.return_home(self.location)
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")

    def return_home(self, home_location: list) -> None:
        self.location = home_location

    def go_shopping(self,
                    fuel_price: float,
                    shops: list[Shop]) -> None:
        self.customers_info()
        (
            cheapest_shop,
            min_total_cost,
            product_cost
        ) = self.look_for_cheapest_shop(fuel_price, shops)

        if cheapest_shop:
            self.make_purchase(cheapest_shop, min_total_cost, product_cost)
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
