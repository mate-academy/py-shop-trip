from math import dist


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list[int],
                 money: float,
                 car_consumption: float) -> None:
        self.name = name
        self.product_cart = product_cart
        self.home = location
        self.location = location
        self.money = money
        self.shop = "Please approve task"
        self.home = location
        self.car_consumption = car_consumption

    def customer_info(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def shop_visit(self, shop_name: str, cost: float) -> None:
        print(f"{self.name}'s trip to the {shop_name} costs {cost}")

    def change_location(self, destination: list) -> None:
        self.location = destination

    def come_back_home(self, spent_money: float) -> None:
        print(f"{self.name} rides home\n"
              f"{self.name} now has {self.money - spent_money} dollars\n")

    def fuel_cost(self,
                  shop_location: list[int],
                  fuel_price: float) -> float:
        fuel = self.car_consumption / 100
        return fuel * fuel_price * dist(self.location, shop_location)
