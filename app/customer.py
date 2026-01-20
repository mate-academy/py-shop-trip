from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str, product_cart: dict,
                 location: list, money: float, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.target_shop = None

    def calculate_all_cost(self, shops: list[Shop], fuel_price: float) -> None:
        total_product_costs_in_each_shop = []
        costs_all_fuel_to_each_shop = []

        for shop in shops:
            cost_road_to_shop = self.car.calculate_road_cost(
                self.location,
                shop.location,
                fuel_price
            )
            costs_all_fuel_to_each_shop.append(cost_road_to_shop)
            costs_product = shop.calculate_product_cost(self.product_cart)
            # append total cost for particular shop
            total_product_costs_in_each_shop.append(sum(costs_product))
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {cost_road_to_shop + sum(costs_product)}")
        # Calculate total costs for each shops
        total_costs = list(map(lambda x, y: x + y,
                               total_product_costs_in_each_shop,
                               costs_all_fuel_to_each_shop))
        # Find cheaper shop
        self.find_cheaper_shop(total_costs, shops)

    def find_cheaper_shop(self, total_costs: list, shops: list[Shop]) -> None:
        index = total_costs.index(min(total_costs))
        if total_costs[index] > self.money:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            self.target_shop = shops[index]
            self.money -= total_costs[index]
            print(f"{self.name} rides to {self.target_shop.name}\n")

    def print_goodbye(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")
