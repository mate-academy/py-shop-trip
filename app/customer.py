import math

from app.shops import Shops


class Customers:
    def __init__(self, customer_dict: dict) -> None:
        self.name = customer_dict["name"]
        self.prod_cart = customer_dict["product_cart"]
        self.location = customer_dict["location"]
        self.money = customer_dict["money"]
        self.car = customer_dict["car"]

    @staticmethod
    def distance_two_points(point_1: list, point_2: list) -> float:
        x1, y1 = point_1
        x2, y2 = point_2
        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def cost_trip(self, market: Shops, fuel_price: float) -> float:
        distance_to_market = self.distance_two_points(
            market.location, self.location
        )
        fuel_cost = 2 * distance_to_market * self.car[
            "fuel_consumption"] / 100 * fuel_price

        money_in_market = Shops.get_total(market, self)
        total_cost = money_in_market + fuel_cost
        return round(total_cost, 2)

    def choice_of_options(self, market: Shops, fuel_price: float) -> None:
        favorite_shop = ""
        print(f"{self.name} has {self.money} dollars")
        dict_cost = {}
        for shop in market.list_of_shops:
            cost_trip = self.cost_trip(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs {cost_trip}")
            dict_cost[shop.name] = cost_trip
        min_money = min(dict_cost.values())
        if self.money > min_money:
            for key, value in dict_cost.items():
                if value == min_money:
                    favorite_shop = key
                    print(f"{self.name} rides to {favorite_shop}\n")
            for shop in market.list_of_shops:
                if shop.name == favorite_shop:
                    Shops.print_receipt(shop, self)
                    print(f"{self.name} rides home")
                    balance_of_money = round(
                        self.money - self.cost_trip(shop, fuel_price
                                                    ), 2)

                    print(f"{self.name} now has {balance_of_money} dollars\n")
        else:
            print(f"{self.name} doesn't have enough "
                  f"money to make purchase in any shop")
