from app.car import Car
from app.shop import Shop
from math import sqrt


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float,
            car: Car,

    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.start_location = location
        self.current_location = location
        self.money = money
        self.car = car
        self.has_enough_money = False
        self.can_spend = 0

    def find_the_cheapest_option(
            self,
            shops:
            list[Shop],
            fuel_price: int | float
    ) -> Shop:
        costs_shops = {}
        print(f"{self.name} has {self.money} dollars")

        for shop in shops:
            distance = sqrt(
                (shop.location[0] - self.start_location[0]) ** 2
                + (shop.location[1] - self.start_location[1]) ** 2
            )
            fuel_cost = (
                distance * self.car.one_km_consumption() * fuel_price
            ) * 2
            products_cost = 0
            for product, count in self.product_cart.items():
                products_cost += (shop.products[product] * count)

            overall_cost = fuel_cost + products_cost
            costs_shops[overall_cost] = shop
            print(f"{self.name}'s trip to the "
                  f"{shop.name} costs {round(overall_cost, 2)}")

        if self.money >= min(costs_shops):
            self.has_enough_money = True
            self.can_spend = min(costs_shops)

        return costs_shops[min(costs_shops)]

    def visit_shop(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.current_location = shop.location
        shop.get_check(self)

    def go_home(self) -> None:
        self.current_location = self.start_location
        self.money -= self.can_spend
        self.can_spend = 0

        print(
            f"{self.name} rides home\n"
            f"{self.name} now has {round(self.money, 2)} dollars\n"
        )

    @classmethod
    def create_customers(cls, customers_config: list) -> list:
        return [
            Customer(
                name=customer["name"],
                product_cart=customer["product_cart"],
                location=customer["location"],
                money=customer["money"],
                car=Car(
                    brand=customer["car"]["brand"],
                    fuel_consumption=customer["car"]["fuel_consumption"]
                )
            )
            for customer in customers_config
        ]
