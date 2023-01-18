from app.info import get_customers_list
from datetime import datetime
from freezegun import freeze_time


class Customer:

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:

        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

        self.car_fuel_consumption_per_km = self.car["fuel_consumption"] / 100

    @freeze_time("01/04/2021 12:33:41")
    def make_prints_for_shop_visit(self, cheapest_shop: dict) -> None:
        if self.money < cheapest_shop["cost"]:
            print(f"{self.name} doesn't have "
                  f"enough money to make purchase in any shop")
        else:
            print(f"{self.name} rides to {cheapest_shop['name']}")
            customer_home_location = self.location
            self.location = cheapest_shop["location"]

            day = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            print(f"\nDate: {day}")
            print(f"Thanks, {self.name}, for you purchase!")
            print("You have bought: ")

            for product_name, quantity in self.product_cart.items():
                print(f"{quantity} {product_name}s "
                      f"for {cheapest_shop[product_name]} dollars")

            print(f"Total cost is {cheapest_shop['products']} dollars")
            print("See you again!")

            print(f"\n{self.name} rides home")
            self.location = customer_home_location

            money_left = self.money - cheapest_shop["final_cost"]

            print(f"{self.name} now has {money_left} dollars\n")

    @staticmethod
    def create_class_instance_customers_list() -> list:
        customers_list = get_customers_list()
        customer_class_list = []
        for customer in customers_list:
            customer_class_list.append(
                Customer(
                    customer["name"],
                    customer["product_cart"],
                    customer["location"],
                    customer["money"],
                    customer["car"]
                )
            )
        return customer_class_list
