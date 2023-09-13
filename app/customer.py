from app.car import Car
from app.shop import Shop
import datetime
from typing import List


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
        self.location = location
        self.money = money
        self.car = car

    @staticmethod
    def is_less(value: float, other: float | None) -> bool:
        if not other:
            return True
        return value < other

    def find_the_cheapest_shop(
        self, shops: List[Shop], fuel_price: float
    ) -> dict | None:
        print(f"{self.name} has {self.money} dollars")
        lowest_costs = None
        result = None
        for shop in shops:
            distance_to_the_shop = shop.calculate_distance(self.location)
            fuel_costs = self.car.calculate_fuel_costs(
                distance_to_the_shop, fuel_price
            )
            shop_response = shop.get_full_receipt(self.product_cart)
            total_costs = fuel_costs + shop_response.get("products_costs")
            shop_response["shop"] = shop.name
            print(
                f"{self.name}'s trip to the {shop.name} costs {total_costs}"
            )
            if self.is_less(total_costs, lowest_costs):
                lowest_costs = total_costs
                result = shop_response
        if self.money >= lowest_costs:
            self.money -= lowest_costs
            print(f"{self.name} rides to {result.get('shop')}\n")
            return result
        print(
            f"{self.name} doesn't have enough money "
            f"to make a purchase in any shop"
        )

    def ride_purchase_ask_the_receipt(self, info: dict) -> None:
        current_datetime = datetime.datetime.now()
        formatted_date_time = current_datetime.strftime("%d/%m/%Y %H:%M:%S")
        products_info, products_value = info.get("order"), info.get(
            "products_costs"
        )

        print(
            f"Date: {formatted_date_time}\nThanks, {self.name}, "
            f"for your purchase!\nYou have bought: "
        )

        for product, info in products_info.items():
            print(
                f"{info.get('quantity')} {product}s "
                f"for {info.get('value')} dollars"
            )
        print(f"Total cost is {products_value} dollars")
        print("See you again!\n")
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")
