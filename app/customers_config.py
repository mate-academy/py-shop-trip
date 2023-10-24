from dataclasses import dataclass


from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    wish_list: {}
    location: []
    money: int
    car: Car

    def pick_the_shop(self) -> None:
        shops = Shop.define_shops()
        costs = {}
        for shop in shops:
            fuel = self.car.fuel_outgo(shop.location, self.location)
            costs[shop.pack_the_bucket(self.wish_list)
                  + self.car.fuel_outgo(shop.location, self.location)] = shop
            print(f"{self.name}'s trip to the {shop.name} costs "
                  f"{shop.pack_the_bucket(self.wish_list) + fuel}")
        min_costs = min(key for key in costs.keys())
        best_shop = costs[min_costs]
        if self.money >= min_costs:
            self.visit_to_shop(best_shop, min_costs)
        else:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")

    def visit_to_shop(self, best_shop: Shop, min_costs: int | float) -> None:
        print(f"{self.name} rides to {best_shop.name}\n")
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {self.name}, for your purchase!\nYou have bought: ")
        for pos in self.wish_list.keys():
            article = best_shop.product_list.get(pos)
            print(f"{self.wish_list.get(pos)} {pos}s for "
                  f"{article * self.wish_list.get(pos)} "
                  f"dollars")
        print(f"Total cost is {(best_shop.pack_the_bucket(self.wish_list))} "
              f"dollars")
        print("See you again!\n")
        self.money -= min_costs
        print(f"{self.name} rides home\n{self.name} "
              f"now has {self.money} dollars\n")

    def customers_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")
        self.pick_the_shop()
