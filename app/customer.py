from decimal import Decimal
from math import sqrt

from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: Decimal,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def cost_product(
        self, price: dict, fuel_price: Decimal, shop_location: list
    ) -> Decimal:
        result_cost = 0
        for key_prod, value_prod in self.product_cart.items():
            for key_price, value_price in price.items():
                if key_prod == key_price:
                    result_cost += Decimal(value_price) * Decimal(value_prod)

        length_way = Decimal(self.count_length_to_shop(shop_location))
        result_cost += self.car.count_fuel_consumption(fuel_price, length_way)

        return round(result_cost, 2)

    def update_person_money(self, spend_money: Decimal) -> None:
        # self.money -= spend_money
        print(f"{self.name} now has {self.money - spend_money} dollars\n")

    def count_length_to_shop(self, shop_location: list) -> float:
        return sqrt(
            (Decimal(shop_location[0]) - Decimal(self.location[0])) ** 2
            + (Decimal(shop_location[1]) - Decimal(self.location[1])) ** 2
        )
