import datetime
from math import inf
from decimal import Decimal
from dataclasses import dataclass
from app.car import Car
from app.shop import Shop


@dataclass()
class Customer:
    name: str
    product_cart: dict
    location: list[int, int]
    money: Decimal
    car: Car

    # calculate distance between customer location and other location
    def calculate_distance(self, goal_location: list[int, int]) -> float:
        dist_x: int = self.location[0] - goal_location[0]
        dist_y: int = self.location[1] - goal_location[1]
        distance = (dist_x ** 2 + dist_y ** 2) ** 0.5
        return distance

    # calculate sum cost of products in product_card for some shop
    def calculate_products_cost(self, shop: Shop) -> Decimal:
        products_cost: Decimal = Decimal("0")
        for needed_product, count in self.product_cart.items():
            for available_product, cost in shop.products.items():
                if needed_product == available_product:
                    products_cost += Decimal(count * Decimal(f"{cost}"))
        return products_cost

    # determination costs of trip for every shop and return shop with min cost
    def determination_min_trip_cost(
            self,
            shops_list: list[Shop],
            fuel_price: Decimal
    ) -> dict:
        customer_shop_min: dict = {
            "customer": self,
            "shop": None,
            "trip_cost": inf
        }
        for shop in shops_list:
            products_cost: Decimal = self.calculate_products_cost(shop)
            distance = self.calculate_distance(shop.location)
            fuel_outlay = distance * self.car.fuel_consumption / 100
            fuel_cost: Decimal = Decimal(str(fuel_outlay)) * fuel_price
            trip_cost: Decimal = \
                Decimal(round(fuel_cost * 2 + products_cost, 2))
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")
            if customer_shop_min["trip_cost"] > trip_cost:
                customer_shop_min["shop"] = shop
                customer_shop_min["trip_cost"] = trip_cost
        return customer_shop_min

    # print purchase receipt for some customer
    def print_purchase_receipt(self, shop: Shop) -> None:
        print(f"\nDate: "
              f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {self.name}, for you purchase!\n"
              f"You have bought: ")
        total_cost: Decimal = Decimal("0")
        for product_need, count in self.product_cart.items():
            for product_available, cost in shop.products.items():
                if product_need == product_available:
                    price: Decimal = Decimal(str(round(count * cost, 1)))
                    total_cost += price
                    print(f"{count} {product_need}s for {price} dollars")
        print(f"Total cost is {total_cost} dollars\n"
              f"See you again!\n")
