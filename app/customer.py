from math import dist

from app.shop import Shop


class Customer:
    def __init__(self, data: dict) -> None:
        self.name: str = data["name"]
        self.product_cart: dict = data["product_cart"]
        self.location: list = data["location"]
        self.home_location: list = data["location"]
        self.money = data["money"]
        self.car = data["car"]

    def plan_shopping(self, shops: list, fuel_price: float) -> tuple:
        print(f"{self.name} has {self.money} dollars")
        options = {}
        for shop in shops:
            fuel_cost = self.calculate_fuel_cost(fuel_price, shop.location) * 2
            goods_cost = self.calculate_goods_cost(shop.products)
            total_cost = round((fuel_cost + goods_cost), 2)
            options[total_cost] = shop
            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")
        return options[min(options)], min(options)

    def calculate_fuel_cost(self,
                            fuel_price: float,
                            shop_location: list) -> float:
        distance = dist(self.location, shop_location)
        return self.car["fuel_consumption"] * distance * fuel_price / 100

    def calculate_goods_cost(self, price_list: list) -> float:
        return sum([amount * price_list[item]
                    for item, amount in self.product_cart.items()])

    def go_shopping(self,
                    shop: Shop,
                    fuel_price: float,
                    overall_cost: float) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location
        fuel_cost = self.calculate_fuel_cost(fuel_price, shop.location) * 2
        self.money -= fuel_cost
        self.money -= overall_cost

    def back_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = self.home_location
        print(f"{self.name} now has {self.money} dollars\n")
