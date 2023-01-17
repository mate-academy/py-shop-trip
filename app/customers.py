from app.info import get_information
from datetime import datetime
from freezegun import freeze_time


class Customer:

    def __init__(self, dictionary: dict) -> None:
        for key, value in dictionary.items():
            setattr(self, key, value)
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
        customers_list = get_information()["customers"]
        customer_class_list = []
        for customer in customers_list:
            customer_class_list.append(Customer(customer))
        return customer_class_list
