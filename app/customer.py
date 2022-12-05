import datetime
import math
from dataclasses import dataclass
from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    location: list
    product_cart: dict
    money: [float, int]
    car: Car

    def choose_shop(self, shops_data: dict) -> Shop:
        shops_costs_for_customer = {
            shop_name: self.shop_visiting_cost(shop_data)
            for shop_name, shop_data in shops_data.items()
        }

        list_of_shop_names = list(shops_costs_for_customer.keys())
        list_of_shops_costs = list(shops_costs_for_customer.values())

        return shops_data[
            list_of_shop_names[
                list_of_shops_costs.index(min(list_of_shops_costs))
            ]
        ]

    def has_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def shop_visiting_cost(self, shop: Shop) -> [float, int]:
        products_procurement_cost = 0
        for product, cost_per_unit in shop.products.items():
            products_procurement_cost += \
                shop.products[product] * self.product_cart[product]

        fuel_cost_per_km = \
            self.car.fuel_consumption * self.car.fuel_price / 100
        distance_cost = \
            math.dist(self.location, shop.location) * fuel_cost_per_km
        cost = round(2 * distance_cost + products_procurement_cost, 2)

        return cost

    def ride_to_shop(self, shops_data: dict) -> bool:
        if self.money >= self.shop_visiting_cost(self.choose_shop(shops_data)):
            return True
        return False

    def customer_purchasing_process(self, shop: Shop) -> object:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")

        total_purchasing_costs = 0
        for product, product_quantity in self.product_cart.items():
            costs_per_product = product_quantity * shop.products[product]
            total_purchasing_costs += costs_per_product
            print(f"{product_quantity} {product}s "
                  f"for {costs_per_product} dollars")

        print(f"Total cost is {total_purchasing_costs} dollars")
        print("See you again!")
        print()
        print(f"{self.name} rides home")
        print(f"{self.name} now has "
              f"{round(self.money - self.shop_visiting_cost(shop), 2)}"
              f" dollars")
        print()

        return total_purchasing_costs
