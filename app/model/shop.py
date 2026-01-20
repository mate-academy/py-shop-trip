import dataclasses
import math
import datetime


@dataclasses.dataclass
class Shop:
    name: str
    loc: list
    products: dict

    def get_shopping_cost(self,
                          customer_loc: list,
                          customer_shopping_cart: dict,
                          customer_car: dict,
                          fuel_price: float):
        total_cost = 0
        for product, qty in customer_shopping_cart.items():
            total_cost += qty * self.products[product]
        distance = math.hypot(customer_loc[0] - self.loc[0],
                              customer_loc[1] - self.loc[1])
        fuel_needed = (distance * customer_car["fuel_consumption"] / 100)
        total_cost += fuel_needed * fuel_price * 2
        return round(total_cost, 2)

    def visit_cheapest_shop(self, customer_name, customer_cart):
        time_now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {time_now}")
        print(f"Thanks, {customer_name}, for you purchase!")
        print("You have bought: ")
        total_cost = 0
        for key, value in customer_cart.items():
            total_cost += value * self.products[key]
            print(f"{value} {key}s for {value * self.products[key]} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
