import dataclasses
from typing import List

from app.car import Car
from app.shop import Shop


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: Car

    @classmethod
    def create_customers(cls, customers: List) -> List:
        customer_objects = []
        for customer in customers:
            car_data = customer.pop("car")
            car = Car(**car_data)
            customer["car"] = car
            customer_objects.append(cls(**customer))
        return customer_objects

    def choose_the_best_shop(self,
                             shops_list: List[Shop],
                             fuel_price: float) -> tuple[Shop, bool]:
        print(f"{self.name} has {self.money} dollars")
        shops = {}
        for shop in shops_list:
            costs_of_product = shop.calculate_amount_for_products(
                self.product_cart
            )
            fuel_cost = self.car.calculate_fuel_cost(self.location,
                                                     shop.location,
                                                     fuel_price)
            shops[shop] = round(costs_of_product + fuel_cost * 2, 2)
            print(f"{self.name}'s trip to the {shop.name} costs {shops[shop]}")
        cheapest_shop = min(shops, key=shops.get)
        enough_money = False
        if self.money >= shops[cheapest_shop]:
            enough_money = True
        return cheapest_shop, enough_money

    def ride_to_the_shop(self,
                         shop: Shop,
                         enough_money: bool,
                         fuel_price: float | int) -> None:
        if enough_money:
            print(f"{self.name} rides to {shop.name}\n")
            self.money -= self.car.calculate_fuel_cost(
                self.location, shop.location, fuel_price
            )
            self.location = shop.location
        else:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")

    def buy_products(self, shop: Shop) -> None:
        self.money -= shop.print_bill(self.product_cart, self.name)

    def ride_to_home(self,
                     home_location: list,
                     fuel_price: float | int) -> None:
        self.money -= self.car.calculate_fuel_cost(
            self.location, home_location, fuel_price
        )
        self.location = home_location
        print(f"{self.name} rides home\n"
              f"{self.name} now has {round(self.money, 2)} dollars\n")
