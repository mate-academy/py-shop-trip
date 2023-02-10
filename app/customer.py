import math


class Shop:
    list_of_shops = []

    def __init__(self, shop_dict: dict) -> None:
        self.name = shop_dict["name"]
        self.location = shop_dict["location"]
        self.product = shop_dict["products"]
        Shop.list_of_shops.append(self)


class Customer:
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

    def get_total_in_shop(self, market: Shop) -> float:
        total_cost = sum(
            [self.prod_cart[product] * market.product[product]
             for product in self.prod_cart])
        return total_cost

    def cost_trip(self, market: Shop, fuel_price: float) -> float:
        distance_to_market = self.distance_two_points(
            market.location, self.location
        )
        fuel_cost = 2 * distance_to_market \
            * (self.car["fuel_consumption"] / 100) \
            * fuel_price
        total_cost = self.get_total_in_shop(market) + fuel_cost
        return round(total_cost, 2)

    def print_receipt(self, market: Shop) -> None:
        print(
            f"Date: 04/01/2021 12:33:41\n"
            f"Thanks, {self.name}, for you purchase!\n"
            f"You have bought: ")
        for product in self.prod_cart:
            print(
                f"{self.prod_cart[product]} {product}s for "
                f"{self.prod_cart[product] * market.product[product]} dollars")
        print(f"Total cost is {self.get_total_in_shop(market)} dollars")
        print("See you again!\n")

    def optimal_shop(self, market: Shop, fuel_price: float) -> None | str:
        favorite_shop = ""
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
        else:
            print(f"{self.name} doesn't have enough "
                  f"money to make purchase in any shop")
            return
        return favorite_shop

    def trip_in_shop(self, market: Shop, fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")
        optimal_shop = self.optimal_shop(market, fuel_price)
        for shop in market.list_of_shops:
            if shop.name == optimal_shop:
                self.print_receipt(shop)
                print(f"{self.name} rides home")
                balance_of_money = round(
                    self.money - self.cost_trip(shop, fuel_price
                                                ), 2)
                print(f"{self.name} now has {balance_of_money} dollars\n")
