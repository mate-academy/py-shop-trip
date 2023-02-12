import math


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home = location

    def calc_fuel_to_location(self, location: list) -> float:
        distance = math.dist(self.location, location)
        return self.car["fuel_consumption"] / 100 * distance

    def calc_shop_visit_cost(self, shops_list: list, fuel_price: float):
        costs = {}
        for shop in shops_list:
            fuel_cost = fuel_price * self.calc_fuel_to_location(shop.location)
            product_cost = 0
            for product, amount in self.product_cart.items():
                product_cost += shop.products[product] * amount
            costs[shop] = round(2 * fuel_cost + product_cost, 2)
        return costs

    def visit_shop(self, shops_list, fuel_price):
        print(f"{self.name} has {self.money} dollars")
        shop_visit_costs = self.calc_shop_visit_cost(
            shops_list, fuel_price
        )
        for shop, cost in shop_visit_costs.items():
            print(f"{self.name}'s trip to the {shop.name} costs {cost}")
        cheapest_shop = min(shop_visit_costs, key=shop_visit_costs.get)
        if self.money < shop_visit_costs[cheapest_shop]:
            print(f"{self.name} doesn't have enough money "
                  f"to make purchase in any shop")
        else:
            print(f"{self.name} rides to {cheapest_shop.name}\n")
            self.location = cheapest_shop.location
            cheapest_shop.print_receipt(self)
            money_left = self.money - shop_visit_costs[cheapest_shop]
            print(f"{self.name} rides home")
            self.location = self.home
            print(f"{self.name} now has {money_left} dollars\n")
