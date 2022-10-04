import dataclasses
import json


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    fuel_consumption: float
    car: dict
    fuel_price: float = 2.4

    @classmethod
    def open_json_customers(cls):
        with open("app/config.json") as json_file:
            config = json.load(json_file)

        customers = []

        for customer in config["customers"]:
            customers.append(
                Customer(
                    customer["name"],
                    customer["product_cart"],
                    customer["location"],
                    customer["money"],
                    customer["car"]["fuel_consumption"],
                    customer["car"]
                )
            )
            return customers

    def print_has_money(self):
        print(f"{self.name} has {self.money} dollars")

    def distance(self, other):
        x = other.location[0] - self.location[0]
        y = other.location[1] - self.location[1]
        distance = (x ** 2 + y ** 2) ** 0.5 * 2
        return round(distance, 2)

    # def total_product_cost(self, other):
    #     total_product_cost = 0
    #     for position in self.product_cart.keys():
    #         total_product_cost += self.product_cart[position] *\
    #                               other.products[position]
    #         return total_product_cost
    #
    # def total_fuel_cost(self, other):
    #     cost_of_one_km = self.car["fuel_consumption"] * self.fuel_price / 100
    #     total_fuel_cost = self.distance(other) * cost_of_one_km
    #     total_fuel = round(total_fuel_cost, 2)
    #     return total_fuel

    def total_product_with_fuel_price(self, other_shop):
        total_product_cost = 0
        for position in self.product_cart.keys():
            total_product_cost += self.product_cart[position] *\
                                  other_shop.products[position]
            cost_of_one_km = self.car["fuel_consumption"] * self.fuel_price / 100
            total_fuel_cost = self.distance(other_shop) * cost_of_one_km
            total_fuel = round(total_fuel_cost, 2)
            return total_product_cost + total_fuel

    def print_go_to_shop(self, other_shop):
        self.location = other_shop.location
        print(f"{self.name} rides to {other_shop.name}\n")

    def print_go_to_home(self):
        print(f"{self.name} rides home")

    def print_change_balance(self, other_shop):
        return f"{self.name} now has" \
               f" {self.money - self.total_product_with_fuel_price(other_shop)}" \
               f" dollars\n"
