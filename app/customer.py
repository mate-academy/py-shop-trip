from datetime import datetime
from app.shop import Shop
from app.car import Car


class Customer:
    picked_shop = None
    costs_travel = 0
    customer_location = [0, 0]

    def __init__(self, name: str, money: int, car: Car) -> None:
        self.name = name
        self.money = money
        self.car = car

    def money_sum(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def cost_trip(self, shop: Shop) -> bool:
        product_cart = shop.product_cart
        shops = shop.shops

        self.customer_location = self.car.location

        min_costs_shop = {}

        for shop in shops:
            distance = self.car.calculate_distance(shop["location"])
            sum_cart = {key: product_cart[key] * shop["products"][key]
                        for key in product_cart}
            cost_travel = (sum(sum_cart.values())
                           + self.car.road_cost(distance))
            print(f"{self.name}'s trip to the "
                  f"{shop['name']} costs {cost_travel}")
            min_costs_shop.update({shop["name"]: cost_travel})

        min_costs_shop_sorted = dict(sorted(min_costs_shop.items(),
                                            key=lambda value: value[1]))

        name_shop, costs = next(iter(min_costs_shop_sorted.items()))

        self.picked_shop = name_shop
        self.costs_travel = costs
        if self.costs_travel > self.money:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            return False

        if self.costs_travel <= self.money:
            print(f"{self.name} rides to {self.picked_shop}")
            # change coord customer on shop coord
            selected_shop = next(shop for shop in shops
                                 if shop["name"] == self.picked_shop)
            self.car.location = selected_shop["location"]

            specific_time = datetime(2021, 4, 1, 12, 33, 41)
            print(f"\nDate: {specific_time.strftime('%m/%d/%Y %H:%M:%S')}")
            print(f"Thanks, {self.name}, for your purchase!")
            return True

    def rides_home(self) -> None:
        print(f"\n{self.name} rides home")

        self.car.location = self.customer_location

        print(f"{self.name} now has "
              f"{self.money - self.costs_travel} dollars\n")
