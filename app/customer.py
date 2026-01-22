from app import utils
from dataclasses import dataclass
from app.shop import Shop
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car

    def __post_init__(self) -> None:
        self.initial_location = self.location.copy()

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = utils.calculate_distance(self.location, shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance, fuel_price)
        result = (shop.calculate_products_cost(self.product_cart)
                  + fuel_cost * 2)
        return utils.round2(result)

    def can_afford_trip(self, shop: Shop, fuel_price: float) -> bool:
        return self.money >= self.calculate_trip_cost(shop, fuel_price)

    def go_to(self, shop: Shop, fuel_price: float) -> None:
        distance = utils.calculate_distance(self.location, shop.location)
        self.money -= self.car.calculate_fuel_cost(distance, fuel_price)
        self.location = shop.location
        print(f"{self.name} rides to {shop.name}")

    def go_home(self, fuel_price: float) -> None:
        distance = utils.calculate_distance(self.location,
                                            self.initial_location)
        self.money -= self.car.calculate_fuel_cost(distance, fuel_price)
        self.location = self.initial_location
        print(f"{self.name} rides home")

    def buy_products(self, shop: Shop) -> None:
        self.money -= shop.calculate_products_cost(self.product_cart)

    def print_receipt(self, shop: Shop) -> None:
        print(f"Date: {utils.get_current_time()}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for item in self.product_cart:
            qty = self.product_cart[item]
            price = shop.products[item]
            cost = utils.from_float_to_int(qty * price)
            print(f"{qty} {item}s for {cost} dollars")
        total = shop.calculate_products_cost(self.product_cart)
        print(f"Total cost is {utils.round2(total)} dollars")
        print("See you again!")
