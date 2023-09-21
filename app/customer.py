import datetime
from dataclasses import dataclass
from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: Car

    def has_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def chip_shop(self, shops: list, fuel: float) -> None:
        cheap_shop = None
        spent_for_shopping = float("inf")
        total_cost = 0
        for shop in shops:
            cost_of_all_goods = round(
                self.car.trip_cost(self.location, shop.location, fuel) * 2
                + shop.purchase_amount(self.product_cart), 2
            )

            print(f"{self.name}'s trip to the "
                  f"{shop.name} costs "
                  f"{cost_of_all_goods}")

            if (cost_of_all_goods <= spent_for_shopping
                    and cost_of_all_goods <= self.money):

                cheap_shop = shop
                spent_for_shopping = cost_of_all_goods

        if cheap_shop:
            print(f"{self.name} rides to {cheap_shop.name}\n")

            self.location = cheap_shop.location

            data = datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S")
            print(f"Date: {data}\nThanks, {self.name}, "
                  f"for your purchase!\nYou have bought: ")

            for key, value in self.product_cart.items():
                total_cost += cheap_shop.products[key] * value

                cost = cheap_shop.products[key] * value
                cost = int(cost) if (isinstance(
                    cost, float) and cost.is_integer()) else cost

                print(f"{value} {key}s for {cost} dollars")

            print(f"Total cost is {total_cost} dollars")

            self.money -= spent_for_shopping

            print("See you again!\n\n"
                  f"{self.name} rides home\n"
                  f"{self.name} now has {self.money} dollars\n")

        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
