import math


class Customer:

    def __init__(self, name: str, product_cart: dict,
                 location: list, money: int, car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def find_distance(self, shop: object) -> float:
        first_part = (shop.location[0] - self.location[0]) ** 2
        second_part = (shop.location[1] - self.location[1]) ** 2
        distance = math.sqrt(first_part + second_part)
        return distance

    def total_expense(self, fuel_price: int, shop: object) -> int:
        one_km_consumption = self.car["fuel_consumption"] / 100
        needed_fuel = self.find_distance(shop) * one_km_consumption
        expense = needed_fuel * fuel_price
        total_road_expense = expense * 2
        groceries_price = shop.total_groceries_cost(self)
        total = round(total_road_expense + groceries_price, 2)
        return total

    def make_choice(self, fuel_price: int, shops_list: list) -> None:
        print(f"{self.name} has {self.money} dollars")
        best_option = shops_list[0]
        cheapest = self.total_expense(fuel_price, shops_list[0])
        for shop in shops_list:
            cost = self.total_expense(fuel_price, shop)
            print(f"{self.name}'s trip to the {shop.name} costs {cost}")
            if cost < cheapest:
                best_option = shop
        money_spent = self.total_expense(fuel_price, best_option)
        if self.money > money_spent:
            print(f"{self.name} rides to {best_option.name}\n")
            best_option.print_receipt(self)
            self.money -= money_spent
            self.go_home()
            return
        print(f"{self.name} doesn't have enough money to "
              f"make purchase in any shop")

    def go_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")
