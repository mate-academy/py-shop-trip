import datetime
import math

from app.customer import Customer
from app.location import Location
from app.shop import Shop


class ShopTripManager:
    def __init__(self, fuel_price: int | float) -> None:
        self._fuel_price = fuel_price

    @property
    def fuel_price(self) -> int | float:
        return self._fuel_price

    def __repr__(self) -> str:
        return f"ShopTripManager(fuel_price={self._fuel_price})"

    def calculate_trip_cost(self, customer: Customer,
                            destination: Shop | Location
                            ) -> float:
        destination = getattr(destination, "location", destination)
        distance = customer.location.distance_to(destination)
        cost = (distance * self._fuel_price
                * customer.car.fuel_consumption / 100)
        return cost

    @staticmethod
    def calculate_shop_cost(customer: Customer, shop: Shop) -> float:
        cost = 0
        for product, price in shop.products.items():
            cost += customer.product_cart.get(product, 0) * price
        return cost

    def calculate_total_cost(self, customer: Customer, shop: Shop) -> float:
        cost = self.calculate_trip_cost(customer, shop) * 2
        cost += self.calculate_shop_cost(customer, shop)
        return cost

    def move_to(self, customer: Customer, shop: Shop) -> None:
        print(f"{customer.name} rides to {shop.name}")
        customer.money -= self.calculate_trip_cost(customer, shop)
        customer.location = shop.location

    def move_home(self, customer: Customer) -> None:
        print(f"{customer.name} rides home")
        customer.money -= self.calculate_trip_cost(customer,
                                                   customer.home_location)
        customer.location = customer.home_location

    def get_cheapest_shop_trip(self,
                               customer: Customer,
                               shops: list[Shop]
                               ) -> Shop | None:
        print(f"{customer.name} has {customer.money} dollars")
        lowest_cost = math.inf
        cheapest_shop = None
        for shop in shops:
            cost = self.calculate_total_cost(customer, shop)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {round(cost, 2)}")
            if cost < lowest_cost:
                lowest_cost = cost
                cheapest_shop = shop
        if customer.money >= lowest_cost:
            return cheapest_shop
        print(f"{customer.name} doesn't have enough money "
              f"to make a purchase in any shop")
        return None

    def do_shopping(self, customer: Customer, shop: Shop) -> None:
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = self.calculate_shop_cost(customer, shop)
        customer.money -= total_cost
        for product, price in shop.products.items():
            quantity = customer.product_cart.get(product, 0)
            print(f"{quantity} {product}s for{(price * quantity): g} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
