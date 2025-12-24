from dataclasses import dataclass

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    location: list
    money: int or float
    car: Car
    product_cart: dict
    selected_shop: Shop = None
    acquisition_costs: float = None
    home_location: list = None

    def has_dollars(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calculate_shop_trip(self, shop: Shop, fuel_price: float) -> float:
        product_cost = 0
        shop_offer = shop.products
        shopping_card = self.product_cart
        for product in shopping_card.keys():
            if product in shop_offer and shop_offer[product]:
                product_cost += shopping_card[product] * shop_offer[product]

        trip_costs = (self.car.trip_consumption(self.location, shop.location)
                      * fuel_price)
        total_costs = round(trip_costs + product_cost, 2)

        print(f"{self.name}'s trip to the {shop.name} costs {total_costs}")
        return total_costs

    def visit_the_shop(self) -> bool or None:
        if self.selected_shop and self.acquisition_costs:

            if self.acquisition_costs > self.money:
                return print(f"{self.name} doesn't have "
                             f"enough money to make a purchase in any shop")

            print(f"{self.name} rides to {self.selected_shop.name}")
            self.home_location = self.location
            self.location = self.selected_shop.location
            return True
        else:
            print(f"{self.name} hasn't decided where wants to rides.")

    def rides_home(self) -> None:
        self.location = self.home_location
        balance = round(self.money - self.acquisition_costs, 2)
        self.money = balance
        print(f"\n{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")
