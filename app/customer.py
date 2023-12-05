from app.shop import Shop
import math
import datetime


class Customer:

    instances = []

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = location
        self.__class__.instances.append(self)

    def road_cost(self, fuel_cost: float = 2.4) -> dict:
        roadcost = {}
        for shop in Shop.instances:
            distance = math.dist(self.home_location, shop.location)
            roadcost[shop.name] = round(self.car["fuel_consumption"]
                                        * distance * 2 * fuel_cost / 100, 2)
        return roadcost

    def groceries_cost(self) -> bool | dict:
        cost_of_groceries = {}
        cost = 0
        products_provided = {}
        for shop in Shop.instances:
            for key, value in self.product_cart.items():
                if key not in shop.products:
                    break
                products_provided[key] = shop.products[key] * value
                cost += value * shop.products[key]
            cost_of_groceries[shop.name] = {
                "total_cost": cost,
                "list": products_provided,
                "location": shop.location
            }
            products_provided = {}
            cost = 0
        if cost_of_groceries:
            return cost_of_groceries
        return False

    def get_receipt(self, groceries: dict, preferable_shop: tuple) -> None:
        shop = groceries[preferable_shop[0]]
        self.location = shop["location"]
        current_date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(
            f"Date: {current_date}\n"
            f"Thanks, {self.name}, for your purchase!\n"
            "You have bought:"
        )
        for key, value in self.product_cart.items():
            price = shop["list"][key]
            print(f"{value} {key}s for{price: g} dollars")
        print(f"Total cost is {shop["total_cost"]} dollars\n"
              f"See you again!\n")
        self.money -= preferable_shop[1]

    def get_home(self) -> None:
        self.location = self.home_location
        print(f"{self.name} rides home\n"
              f"{self.name} now has {self.money} dollars\n")
