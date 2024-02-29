from math import dist
from app.shop import Shop
from app.statics_methods import Method


class Customer:
    def __init__(self, customer_data: dict) -> None:
        self.customer_data = customer_data
        self.name = self.customer_data["name"]
        self.product_cart = self.customer_data["product_cart"]
        self.location = self.customer_data["location"]
        self.money = self.customer_data["money"]
        self.car = self.customer_data["car"]

    def print_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def customer_trip_to_shops(self, json_file: dict) -> tuple:
        totals_of_shop = []
        minimal_price, best_shop = None, None
        fuel_cost = json_file["FUEL_PRICE"]
        for index, element in enumerate(json_file["shops"]):
            shop = Shop(element)
            fuel_cons = self.car["fuel_consumption"]
            distance = dist(self.location, shop.location)
            cost_trip = Method.cost_of_trip(distance, fuel_cons, fuel_cost)
            total_eval = cost_trip * 2 + Method.check_money(
                self.product_cart, shop.products
            )
            totals_of_shop.append(total_eval)

            # Check best prise considering car trip:
            if index == 0:
                minimal_price = total_eval
                best_shop = index
            elif total_eval < minimal_price:
                minimal_price = total_eval
                best_shop = index
            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs{total_eval: .2f}"
            )
        return totals_of_shop, (minimal_price, best_shop)

    def check_perf_purchase(self,
                            shop_data: tuple,
                            json_data: dict
                            ) -> bool:
        shop_index = shop_data[1][1]
        shop = Shop(json_data["shops"][shop_index])
        if self.money < shop_data[1][0] + Method.check_money(
                self.product_cart, shop.products
        ):
            print(
                f"{self.name} doesn't have enough money to make a "
                f"purchase in any shop"
            )
            return False
        else:
            print(f"{self.name} rides to {shop.name}")
            self.location = shop.location
            return True
