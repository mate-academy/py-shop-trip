import datetime
from app.parse_all import ParseJsonMixin
from app.shop import Shop
from app.car import Car


class Customer(ParseJsonMixin):
    customers = []

    def __init__(
            self,
            name: str = None,
            product_cart: dict = None,
            location: list[int] = None,
            money: int = None,
            car: Car = None,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)
        self.full_cost = {}
        self.chosen_shop = None
        Customer.customers.append(self)

    def calculate_costs_shopping_per_shop(self) -> None:
        for shop in Shop.all_shops:
            self.full_cost[shop.name] = 0
            for product in self.product_cart.keys():
                self.full_cost[shop.name] += (shop.products[product]
                                              * self.product_cart[product])
            way_to_shop = self.car.cost_of_way(shop.location, self.location)
            self.full_cost[shop.name] += way_to_shop
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {self.full_cost[shop.name]}")

    def choose_cheapest_shop(self) -> None:
        lowest_cost = min(self.full_cost.values())
        cheapest = {
            key: value
            for key, value
            in self.full_cost.items()
            if value == lowest_cost
        }
        if list(cheapest.values())[0] < self.money:
            for shop in Shop.all_shops:
                if shop.name == list(cheapest.keys())[0]:
                    self.chosen_shop = shop
            print(f"{self.name} rides to {self.chosen_shop.name}\n")

    def bill_shipping(self) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if not self.chosen_shop:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            return
        print(f"Date: {now}\n"
              f"Thanks, {self.name}, for your purchase!\n"
              "You have bought:")
        total_cost = 0
        for name in self.product_cart.keys():
            cost = self.chosen_shop.products[name] * self.product_cart[name]
            if cost == int(cost):
                cost = int(cost)
            print(f"{self.product_cart[name]} {name}s "
                  f"for {cost} dollars")
            total_cost += cost
        print(f"Total cost is {total_cost} dollars\nSee you again!\n")
        print(f"{self.name} rides home")
        print(f"{self.name} now has "
              f"{self.money - self.full_cost[self.chosen_shop.name]} "
              f"dollars\n")
