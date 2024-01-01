from datetime import datetime

from app.car import Car


class Customer:
    picked_shop = None
    costs_travel = 0

    def __init__(self, name: str, money: int) -> None:
        self.name = name
        self.money = money

    def money_sum(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def cost_trip(self, car: Car, product_cart: dict, shops: list) -> bool:
        min_costs_shop = {}

        for shop in shops:
            distance = car.calculate_distance(shop["location"])
            sum_cart = {key: product_cart[key] * shop["products"][key]
                        for key in product_cart}
            cost_travel = (sum(sum_cart.values()) + car.road_cost(distance))
            print(f"{self.name}'s trip to the "
                  f"{shop['name']} costs {cost_travel}")
            min_costs_shop.update({shop["name"]: cost_travel})

        min_costs_shop_sorted = dict(sorted(min_costs_shop.items(),
                                            key=lambda value: value[1]))

        name_shop, costs = next(iter(min_costs_shop_sorted.items()))

        self.picked_shop = name_shop
        self.costs_travel = costs
        if costs > self.money:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            return False

        if costs <= self.money:
            print(f"{self.name} rides to {name_shop}")
            date_time_obj = datetime.now()
            print(f"\nDate: {date_time_obj.strftime('%m/%d/%Y %H:%M:%S')}")
            print(f"Thanks, {self.name}, for your purchase!")
            return True

    def rides_home(self) -> None:
        print(f"\n{self.name} rides home")
        print(f"{self.name} now has "
              f"{self.money - self.costs_travel} dollars\n")
