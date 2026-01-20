from dataclasses import dataclass
import math


from app.classes.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int
    car: Car

    def print_info(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calculate_distance_to_shop(
            self,
            shop_location: list[int]
    ) -> float:
        return math.sqrt(
            (self.location[0] - shop_location[0])**2
            + (self.location[1] - shop_location[1])**2
        )

    def calculate_cost_shopping(self, shop: object, fuel_price: float) -> str:
        distance = self.calculate_distance_to_shop(shop.location)
        way_cost = self.car.calculate_cost_way(distance, fuel_price)
        product_cost = sum(
            self.product_cart[product] * shop.products[product]
            for product in self.product_cart
        )
        total_price = round((way_cost * 2 + product_cost), 2)
        return total_price

    def back_home(self, shops: list, fuel_price: float) -> None:
        if not self.is_enough_money:
            return
        current_shop = None
        for shop in shops:
            if self.shop == shop.name:
                current_shop = shop
        distance = self.calculate_distance_to_shop(current_shop.location)
        way_cost = self.car.calculate_cost_way(distance, fuel_price)
        self.spent_money += round((way_cost * 2), 2)
        print(f"{self.name} rides home\n"
              f"{self.name} now has "
              f"{round((self.money - self.spent_money), 2)} dollars\n")
