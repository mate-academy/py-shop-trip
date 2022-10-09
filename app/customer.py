from math import dist


class Customer:

    def __init__(self,
                 name: str,
                 products_cart: dict,
                 location: list,
                 money: int,
                 car: dict) -> None:
        self.name = name
        self.products_cart = products_cart
        self.location = location
        self.money = money
        self.car = car

    def has_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def get_cost_trip(self, shop_location: list, fuel_price: float) -> float:
        distance = dist(self.location, shop_location)
        fuel_needed = (distance / 100) * self.car["fuel_consumption"]
        cost_trip = fuel_needed * fuel_price
        return cost_trip * 2

    def count_remaining_money(self, all_expenses: float) -> None:
        amount = round(self.money - all_expenses, 2)
        print(f"{self.name} now has {amount} dollars\n")


def make_list_customers(data: dict) -> list:
    customers = []

    for i, customer in enumerate(data["customers"]):
        customers.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer["car"]
            )
        )
    return customers
