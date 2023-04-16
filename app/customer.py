from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart_items: dict,
            location: list[int, int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart_items = product_cart_items
        self.location = location
        self.money = money
        self.car = car

    def pick_the_shop(self) -> None:
        shops = Shop.define_shop()
        costs = {}
        for shop in shops:
            fuel = self.car.calculate_fuel_consumption_price(
                self.location, shop.shop_location)
            costs[
                shop.cart_price(
                    self.product_cart_items
                ) + fuel] = shop
            print(f"{self.name}'s trip to the {shop.name} costs "
                  f"{shop.cart_price(self.product_cart_items) + fuel}")
        min_cost = min(key for key in costs.keys())
        best_shop = costs[min_cost]
        if self.money >= min_cost:
            self.visit_to_shop(best_shop, min_cost)
            self.location = best_shop.shop_location
        else:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")

    def visit_to_shop(self, best_shop: Shop, min_costs: int | float) -> None:
        print(f"{self.name} rides to {best_shop.name}\n")
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {self.name}, for your purchase!\nYou have bought: ")
        for pos in self.product_cart_items.keys():
            article = best_shop.product_list.get(pos)
            print(f"{self.product_cart_items.get(pos)} {pos}s for "
                  f"{article * self.product_cart_items.get(pos)} "
                  f"dollars")
        print(f"Total cost "
              f"is {(best_shop.cart_price(self.product_cart_items))} "
              f"dollars")
        print("See you again!\n")
        self.money -= min_costs
        print(f"{self.name} rides home\n{self.name} "
              f"now has {self.money} dollars\n")

    def customers_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")
        self.pick_the_shop()
